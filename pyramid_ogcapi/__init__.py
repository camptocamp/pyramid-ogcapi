"""Pyramid OGC API extension."""

import json
import logging
from typing import Any, Callable, Dict, List, Optional, cast

import pyramid.config
import pyramid.request

_LOG = logging.getLogger(__name__)


def includeme(config: pyramid.config.Configurator) -> None:
    """Include the OGC API extension."""
    config.include("pyramid_openapi3")
    config.add_directive("pyramid_ogcapi_register_routes", register_routes)


class _OgcType:
    def __init__(self, val: str, config: pyramid.config.Configurator):
        del config
        self.val = val

    def phash(self) -> str:
        """Return a string that uniquely identifies the predicate."""

        return f"ogc_type = {self.val}"

    def __call__(self, context: Any, request: pyramid.request.Request) -> bool:
        """Return a true value if the predicate should be used."""

        del context

        if request.params.get("f") in ["html", "json"]:
            return request.params["f"].lower() == self.val  # type: ignore
        return request.accept.best_match(["text/html", "application/json"]).split("/")[1] == self.val  # type: ignore


def _get_view(
    views: Any, method_config: Any, route_name: str, path: str, helps: List[str], with_help: bool = True
) -> Optional[Callable[[pyramid.request.Request], Any]]:
    example = (
        method_config.get("responses", {})
        .get("200", {})
        .get("content", {})
        .get("application/json", {})
        .get("example", {})
    )
    description = method_config.get("description", "")
    description = description.content() if hasattr(description, "content") else description
    if description:
        description = "\n\n        " + description

    if with_help:
        helps.append(
            f'''
    @pyramid_ogcapi.typed_request
    def {route_name.lower()}(self, pyramid_request: pyramid.request.Request, request: Any) -> Any:
        """
        Get the result for the path '{path}'.{description}
        """

        return {example.content() if hasattr(example, 'content') else example}'''
        )

    if hasattr(views, route_name.lower()):
        return cast(Callable[[pyramid.request.Request], Any], getattr(views, route_name.lower()))
    _LOG.error("Missing view named '%s'", route_name.lower())

    return None


def register_routes(
    config: pyramid.config.Configurator,
    views: Any,
    apiname: str = "pyramid_openapi3",
    route_prefix: Optional[str] = None,
    path_template: Optional[Dict[str, str]] = None,
    json_renderer: str = "json",
) -> None:
    """
    Register routes of an OSC API application.

    :param route_name_ext: Extension's key for using a ``route_name`` argument
    :param root_factory_ext: Extension's key for using a ``factory`` argument
    """

    if path_template is None:
        path_template = {}

    def action() -> None:
        assert path_template is not None

        config.add_route_predicate("ogc_type", _OgcType)

        spec = config.registry.settings[apiname]["spec"]
        helps: List[str] = []
        for pattern, path_config in spec.get("paths", {}).items():
            route_name = ("" if route_prefix is None else route_prefix) + cast(
                str,
                "landing_page"
                if pattern == "/"
                else pattern.lstrip("/")
                .replace("/", "_")
                .replace("{", "")
                .replace("}", "")
                .replace("-", "_"),
            )

            for method, method_config in path_config.items():
                if method == "get":
                    config.add_route(
                        f"{route_name}_html",
                        pattern,
                        request_method="GET",
                        ogc_type="html",
                    )
                    config.add_view(
                        _get_view(views, method_config, route_name, pattern, helps),
                        route_name=f"{route_name}_html",
                        renderer=json_renderer,
                        openapi=True,
                    )
                    config.add_route(
                        f"{route_name}_json",
                        pattern,
                        request_method="GET",
                        ogc_type="json",
                    )
                    config.add_view(
                        _get_view(views, method_config, route_name, pattern, helps, with_help=False),
                        route_name=f"{route_name}_json",
                        renderer=json_renderer,
                        openapi=True,
                    )

                else:
                    route_name += f"_{method}"
                    config.add_route(
                        route_name,
                        pattern,
                        request_method=method.upper(),
                    )
                    config.add_view(
                        _get_view(views, method_config, route_name, pattern, helps),
                        route_name=route_name,
                        renderer=json_renderer,
                        openapi=True,
                    )
        _LOG.debug("Use the following code to add it:\n%s", "\n\n".join(helps))

    config.action(("pyramid_openapi3_register_routes",), action, order=pyramid.config.PHASE1_CONFIG)


def typed_request(
    func: Callable[[Any, pyramid.request.Request, Any], Any]
) -> Callable[[Any, pyramid.request.Request], Any]:
    """
    Decorate for openapi views to have a typed request.

    To be used with the generated types by jsonschema_gentype
    """

    def wrapper(obj: Any, request: pyramid.request.Request) -> Any:
        _typed_request: Dict[str, Any] = {}
        try:
            _typed_request["request_body"] = request.json_body
        except json.JSONDecodeError:
            pass
        _typed_request["path"] = request.matchdict
        _typed_request["query"] = request.params

        return func(obj, request, _typed_request)

    return wrapper
