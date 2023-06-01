"""
Generate links for the landing page of the API.
"""

import pyramid.request


def self_link(request: pyramid.request.Request, title: str) -> dict:
    """Return a link to the current landing page."""
    return {"href": request.current_route_url(), "rel": "self", "type": "application/json", "title": title}


def link(request: pyramid.request.Request, api_name: str, path: str, relation_type: str):
    """Return a link to an endpoint specified by its path and link relation type."""
    spec = request.registry.settings[api_name]["spec"]
    return {
        "href": request.application_url + path,
        "rel": relation_type,
        "type": "application/json",
        "title": spec["paths"][path]["get"]["summary"],
    }
