"""
Pyramid OGC API extension.
"""

import logging
from typing import Any, Dict, Optional, cast

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
            _LOG.error(request.params["f"].lower() == self.val)
            return request.params["f"].lower() == self.val  # type: ignore
        _LOG.error(dict(request.headers))
        if request.headers.get("Accept", "*/*") == "*/*":
            return self.val == "json"
        return request.accept.best_match(["text/html", "application/json"]).split("/")[1] == self.val  # type: ignore


def register_routes(
    config: pyramid.config.Configurator,
    path_view: Dict[str, Any],
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
        for pattern in spec["paths"].keys():
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

            if pattern in path_template:
                config.add_route(
                    f"{route_name}_html",
                    pattern,
                    request_method="GET",
                    ogc_type="html",
                )
                config.add_view(
                    path_view[route_name],
                    route_name=f"{route_name}_html",
                    renderer=json_renderer,
                    ogcapi=True,
                )
                config.add_route(
                    f"{route_name}_json",
                    pattern,
                    request_method="GET",
                    ogc_type="json",
                )
                config.add_view(
                    path_view[route_name],
                    route_name=f"{route_name}_json",
                    renderer=json_renderer,
                    ogcapi=True,
                )

            else:
                config.add_route(
                    route_name,
                    pattern,
                    request_method="GET",
                )
                config.add_view(
                    path_view[route_name], route_name=route_name, renderer=json_renderer, ogcapi=True
                )

    config.action(("pyramid_openapi3_register_routes",), action, order=pyramid.config.PHASE1_CONFIG)
