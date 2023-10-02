"""
Pyramid OGC API Features extension.
"""

from typing import Any

import pyramid.config
import pyramid.request

import pyramid_ogcapi
from pyramid_ogcapi import links


def includeme(config: pyramid.config.Configurator) -> None:
    """
    Include the OGC API Features extension.
    """

    config.include(pyramid_ogcapi.includeme)
    apiname = "ogcapi_features"
    config.pyramid_openapi3_spec("/app/ogcapi-features-schema.yaml", apiname=apiname)
    config.pyramid_openapi3_add_explorer(apiname=apiname)
    config.pyramid_ogcapi_register_routes(apiname=apiname, views=_Views(apiname))


class _Views:
    def __init__(self, api_name: str):
        self.api_name = api_name

    @pyramid_ogcapi.typed_request
    def landing_page(self, pyramid_request: pyramid.request.Request, request: Any) -> Any:
        """
        Get the result for the path: '/'.

        The landing page provides links to the API definition, the conformance
        statements and to the feature collections in this dataset.
        """
        del request  # Unused

        return {
            "title": "Buildings in Bonn",
            "description": "Access to data about buildings in the city of Bonn via a Web API that conforms to the OGC API Features specification.",
            "links": [
                links.self_link(pyramid_request),
                {
                    "href": "http://data.example.org/api",
                    "rel": "service-desc",
                    "type": "application/vnd.oai.openapi+json;version=3.0",
                    "title": "the API definition",
                },
                {
                    "href": "http://data.example.org/api.html",
                    "rel": "service-doc",
                    "type": "text/html",
                    "title": "the API documentation",
                },
                *links.sub_links(pyramid_request, self.api_name),
            ],
        }

    @pyramid_ogcapi.typed_request
    def conformance(self, pyramid_request: pyramid.request.Request, request: Any) -> Any:
        """
        Get the result for the path: '/conformance'.

        A list of all conformance classes specified in a standard that the
        server conforms to.
        """
        del pyramid_request, request  # Unused

        return {
            "conformsTo": [
                "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core",
                "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30",
                "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/html",
                "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson",
            ]
        }

    @pyramid_ogcapi.typed_request
    def collections(self, pyramid_request: pyramid.request.Request, request: Any) -> Any:
        """
        Get the result for the path: '/collections'.
        """
        del pyramid_request, request  # Unused

        return {
            "links": [
                {
                    "href": "http://data.example.org/collections.json",
                    "rel": "self",
                    "type": "application/json",
                    "title": "this document",
                },
                {
                    "href": "http://data.example.org/collections.html",
                    "rel": "alternate",
                    "type": "text/html",
                    "title": "this document as HTML",
                },
                {
                    "href": "http://schemas.example.org/1.0/buildings.xsd",
                    "rel": "describedby",
                    "type": "application/xml",
                    "title": "GML application schema for Acme Corporation building data",
                },
                {
                    "href": "http://download.example.org/buildings.gpkg",
                    "rel": "enclosure",
                    "type": "application/geopackage+sqlite3",
                    "title": "Bulk download (GeoPackage)",
                    "length": 472546,
                },
            ],
            "collections": [
                {
                    "id": "buildings",
                    "title": "Buildings",
                    "description": "Buildings in the city of Bonn.",
                    "extent": {
                        "spatial": {"bbox": [[7.01, 50.63, 7.22, 50.78]]},
                        "temporal": {"interval": [["2010-02-15T12:34:56Z", None]]},
                    },
                    "links": [
                        {
                            "href": "http://data.example.org/collections/buildings/items",
                            "rel": "items",
                            "type": "application/geo+json",
                            "title": "Buildings",
                        },
                        {
                            "href": "http://data.example.org/collections/buildings/items.html",
                            "rel": "items",
                            "type": "text/html",
                            "title": "Buildings",
                        },
                        {
                            "href": "https://creativecommons.org/publicdomain/zero/1.0/",
                            "rel": "license",
                            "type": "text/html",
                            "title": "CC0-1.0",
                        },
                        {
                            "href": "https://creativecommons.org/publicdomain/zero/1.0/rdf",
                            "rel": "license",
                            "type": "application/rdf+xml",
                            "title": "CC0-1.0",
                        },
                    ],
                }
            ],
        }

    @pyramid_ogcapi.typed_request
    def collections_collectionid(self, pyramid_request: pyramid.request.Request, request: Any) -> Any:
        """
        Get the result for the path: '/collections/{collectionId}'.
        """
        del pyramid_request, request  # Unused

        return {
            "id": "buildings",
            "title": "Buildings",
            "description": "Buildings in the city of Bonn.",
            "extent": {
                "spatial": {"bbox": [[7.01, 50.63, 7.22, 50.78]]},
                "temporal": {"interval": [["2010-02-15T12:34:56Z", None]]},
            },
            "links": [
                {
                    "href": "http://data.example.org/collections/buildings/items",
                    "rel": "items",
                    "type": "application/geo+json",
                    "title": "Buildings",
                },
                {
                    "href": "http://data.example.org/collections/buildings/items.html",
                    "rel": "items",
                    "type": "text/html",
                    "title": "Buildings",
                },
                {
                    "href": "https://creativecommons.org/publicdomain/zero/1.0/",
                    "rel": "license",
                    "type": "text/html",
                    "title": "CC0-1.0",
                },
                {
                    "href": "https://creativecommons.org/publicdomain/zero/1.0/rdf",
                    "rel": "license",
                    "type": "application/rdf+xml",
                    "title": "CC0-1.0",
                },
            ],
        }

    @pyramid_ogcapi.typed_request
    def collections_collectionid_items(self, pyramid_request: pyramid.request.Request, request: Any) -> Any:
        """
        Get the result for the path: '/collections/{collectionId}/items'.

        Fetch features of the feature collection with id `collectionId`.

        Every feature in a dataset belongs to a collection. A dataset may
        consist of multiple feature collections. A feature collection is often a
        collection of features of a similar type, based on a common schema.

        Use content negotiation to request HTML or GeoJSON.
        """
        del pyramid_request, request  # Unused

        return {}

    @pyramid_ogcapi.typed_request
    def collections_collectionid_items_featureid(
        self, pyramid_request: pyramid.request.Request, request: Any
    ) -> Any:
        """
        Get the result for the path: '/collections/{collectionId}/items/{featureId}'.

        Fetch the feature with id `featureId` in the feature collection
        with id `collectionId`.

        Use content negotiation to request HTML or GeoJSON.
        """
        del pyramid_request, request  # Unused

        return {}
