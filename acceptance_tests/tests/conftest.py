import pytest
from pyramid import testing
from pyramid.paster import bootstrap
from webtest import TestApp as WebTestApp  # Avoid warning with pytest


@pytest.fixture(scope="session")
def app_env():
    file_name = "tests.ini"
    with bootstrap(file_name) as env:
        yield env


@pytest.fixture(scope="session")
@pytest.mark.usefixtures("app_env")
def app(app_env):
    config = testing.setUp(registry=app_env["registry"])
    app = config.make_wsgi_app()
    yield app


@pytest.fixture(scope="session")  # noqa: ignore=F811
@pytest.mark.usefixtures("app")
def test_app(request, app):
    testapp = WebTestApp(app)
    yield testapp
