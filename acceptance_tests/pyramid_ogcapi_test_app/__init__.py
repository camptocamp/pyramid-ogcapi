"""
An example application for testing.
"""

from typing import Any

import c2cwsgiutils.pyramid
import sqlalchemy
from c2cwsgiutils.health_check import HealthCheck
from pyramid.config import Configurator

import pyramid_ogcapi_test_app.ogcapi


def main(_: Any, **settings: dict[str, Any]) -> Any:
    """Create a Pyramid WSGI application."""

    config = Configurator(settings=settings)
    config.include(c2cwsgiutils.pyramid.includeme)
    config.include("pyramid_mako")
    dbsession = c2cwsgiutils.db.init(config, "sqlalchemy")

    health_check = HealthCheck(config)
    health_check.add_db_session_check(
        dbsession, query_cb=lambda session: session.execute(sqlalchemy.text("SELECT 1")).fetchall()[0][0]  # type: ignore
    )

    config.include(pyramid_ogcapi_test_app.ogcapi.includeme, route_prefix="/ogcapi")

    return config.make_wsgi_app()
