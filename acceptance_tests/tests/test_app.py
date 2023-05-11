import pytest


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
