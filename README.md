# Pyramid OGC API

Tools used to facilitate the development of OGC API services with Pyramid.

## Installation

```bash
python3 -m pip install pyramid-ogcapi
```

## Getting started

Get the OGC API bundled specifications from the [OGC GitHub organization](https://github.com/opengeospatial/),
and save it as `ogcapi-bundled.json`.

Add in your configuration:

```python
config.include("pyramid_ogcapi")
config.pyramid_openapi3_spec('ogcapi-bundled.json', apiname='ogcapi')
config.pyramid_openapi3_add_explorer(apiname='ogcapi')
config.pyramid_ogcapi_register_routes(apiname='ogcapi')
```

Integrate with [jsonschema_gentypes](https://pypi.org/project/jsonschema-gentypes/).

Add the following views:

```python

from pyramid import view_config
from pyramid_ogcapi import request_dict
from .ogcapi import OgcapiCollectionsCollectionidGet, OgcapiCollectionsCollectionidGetResponse

@request_dict
def myview(
  request: pyramid.request.Request,
  request_typed: OgcapiCollectionsCollectionidGet,
) -> OgcapiCollectionsCollectionidGetResponse:
    return {...}

```

Integrate with [jsonschema_gentypes](https://pypi.org/project/jsonschema-gentypes/)

## Contributing

Install the pre-commit hooks:

```bash
pip install pre-commit
pre-commit install --allow-missing-config
```

The `prospector` tests should pass.

The code should be typed.

The code should be tested with `pytests`.
