import os

import pytest
from c2cwsgiutils.acceptance import image


@pytest.mark.usefixtures("test_app")
def test_docs(test_app):
    response = test_app.get("/ogcapi/docs/")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/html; charset=UTF-8"


@pytest.mark.parametrize(
    "accept,f_param,expected",
    [
        (
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            None,
            "text/html; charset=UTF-8",
        ),
        ("application/json", None, "application/json"),
        (
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "json",
            "application/json",
        ),
        ("application/json", "html", "text/html; charset=UTF-8"),
    ],
)
@pytest.mark.usefixtures("test_app")
def test_api(test_app, accept, f_param, expected):
    response = test_app.get(
        "/ogcapi/", headers={"Accept": accept}, params={"f": f_param} if f_param else None
    )
    assert response.status_code == 200
    assert response.headers["Content-Type"] == expected


# Not working because we can't set the Host header to localhost:9123
# def test_ogcapi():
#    image.check_screenshot(
#        "http://localhost:8080/ogcapi/",
#        headers={"Accept": "text/html", "Host": "localhost:9123"},
#        width=500,
#        height=500,
#        result_folder="results",
#        expected_filename=os.path.join(os.path.dirname(__file__), "ogcapi.expected.png"),
#    )


def test_docs():
    image.check_screenshot(
        "http://localhost:8080/ogcapi/docs/",
        width=900,
        height=900,
        result_folder="results",
        expected_filename=os.path.join(os.path.dirname(__file__), "docs.expected.png"),
    )
