"""
Automatically generated file from a JSON schema.
"""


from typing import Any, Literal, TypedDict, Union

from typing_extensions import Required


class CollectionsCollectionidGet(TypedDict, total=False):
    """
    Description of request on path '/collections/{collectionId}', using method 'get'.

    describe the feature collection with id `collectionId`
    """

    path: Required["CollectionsCollectionidGetPath"]
    """ Required property """

    response: "CollectionsCollectionidGetResponse"


class CollectionsCollectionidGetPath(TypedDict, total=False):
    """
    Parameter type 'path' of request on path '/collections/{collectionId}', using method 'get'.

    Request summary:
    describe the feature collection with id `collectionId`
    """

    collectionId: Required[str]
    """ Required property """


CollectionsCollectionidGetResponse = Union[
    "CollectionsCollectionidGetResponse200", "CollectionsCollectionidGetResponse500"
]


class CollectionsCollectionidGetResponse200(TypedDict, total=False):
    id: Required[str]
    """
    identifier of the collection used, for example, in URIs

    example: address

    Required property
    """

    title: str
    """
    human readable title of the collection

    example: address
    """

    description: str
    """
    a description of the features in the collection

    example: An address.
    """

    links: Required[list["_Collectionscollectionidgetresponse200LinksItem"]]
    """ Required property """

    extent: "_Collectionscollectionidgetresponse200Extent"
    itemType: str
    """
    indicator about the type of the items in the collection (the default value is 'feature').

    default: feature
    """

    crs: list[str]
    """
    the list of coordinate reference systems supported by the service

    default:
      - http://www.opengis.net/def/crs/OGC/1.3/CRS84
    """


class CollectionsCollectionidGetResponse500(TypedDict, total=False):
    """Information about the exception: an error code plus an optional description."""

    code: Required[str]
    """ Required property """

    description: str


class CollectionsCollectionidItemsFeatureidGet(TypedDict, total=False):
    """
    Description of request on path '/collections/{collectionId}/items/{featureId}', using method 'get'.

    fetch a single feature
    """

    path: Required["CollectionsCollectionidItemsFeatureidGetPath"]
    """ Required property """

    response: "CollectionsCollectionidItemsFeatureidGetResponse"


class CollectionsCollectionidItemsFeatureidGetPath(TypedDict, total=False):
    """
    Parameter type 'path' of request on path '/collections/{collectionId}/items/{featureId}', using method 'get'.

    Request summary:
    fetch a single feature
    """

    collectionId: Required[str]
    """ Required property """

    featureId: Required[str]
    """ Required property """


CollectionsCollectionidItemsFeatureidGetResponse = Union[
    "CollectionsCollectionidItemsFeatureidGetResponse500"
]


class CollectionsCollectionidItemsFeatureidGetResponse500(TypedDict, total=False):
    """Information about the exception: an error code plus an optional description."""

    code: Required[str]
    """ Required property """

    description: str


class CollectionsCollectionidItemsGet(TypedDict, total=False):
    """
    Description of request on path '/collections/{collectionId}/items', using method 'get'.

    fetch features
    """

    path: Required["CollectionsCollectionidItemsGetPath"]
    """ Required property """

    query: Required["CollectionsCollectionidItemsGetQuery"]
    """ Required property """

    response: "CollectionsCollectionidItemsGetResponse"


class CollectionsCollectionidItemsGetPath(TypedDict, total=False):
    """
    Parameter type 'path' of request on path '/collections/{collectionId}/items', using method 'get'.

    Request summary:
    fetch features
    """

    collectionId: Required[str]
    """ Required property """


class CollectionsCollectionidItemsGetQuery(TypedDict, total=False):
    """
    Parameter type 'query' of request on path '/collections/{collectionId}/items', using method 'get'.

    Request summary:
    fetch features
    """

    limit: "CollectionsCollectionidItemsGetQueryLimit"
    bbox: list[Union[int, float]]
    datetime: str


CollectionsCollectionidItemsGetQueryLimit = int
"""
minimum: 1
maximum: 10000
default: 10
"""


CollectionsCollectionidItemsGetResponse = Union[
    "CollectionsCollectionidItemsGetResponse400", "CollectionsCollectionidItemsGetResponse500"
]


class CollectionsCollectionidItemsGetResponse400(TypedDict, total=False):
    """Information about the exception: an error code plus an optional description."""

    code: Required[str]
    """ Required property """

    description: str


class CollectionsCollectionidItemsGetResponse500(TypedDict, total=False):
    """Information about the exception: an error code plus an optional description."""

    code: Required[str]
    """ Required property """

    description: str


class CollectionsGet(TypedDict, total=False):
    """
    Description of request on path '/collections', using method 'get'.

    the feature collections in the dataset
    """

    response: "CollectionsGetResponse"


CollectionsGetResponse = Union["CollectionsGetResponse200", "CollectionsGetResponse500"]


class CollectionsGetResponse200(TypedDict, total=False):
    links: Required[list["_ComponentsSchemasLink"]]
    """ Required property """

    collections: Required[list["_ComponentsSchemasCollection"]]
    """ Required property """


class CollectionsGetResponse500(TypedDict, total=False):
    """Information about the exception: an error code plus an optional description."""

    code: Required[str]
    """ Required property """

    description: str


class ConformanceGet(TypedDict, total=False):
    """
    Description of request on path '/conformance', using method 'get'.

    information about specifications that this API conforms to
    """

    response: "ConformanceGetResponse"


ConformanceGetResponse = Union["ConformanceGetResponse200", "ConformanceGetResponse500"]


class ConformanceGetResponse200(TypedDict, total=False):
    conformsTo: Required[list[str]]
    """ Required property """


class ConformanceGetResponse500(TypedDict, total=False):
    """Information about the exception: an error code plus an optional description."""

    code: Required[str]
    """ Required property """

    description: str


class Get(TypedDict, total=False):
    """
    Description of request on path '/', using method 'get'.

    landing page
    """

    response: "GetResponse"


GetResponse = Union["GetResponse200", "GetResponse500"]


class GetResponse200(TypedDict, total=False):
    title: str
    """ example: Buildings in Bonn """

    description: str
    """ example: Access to data about buildings in the city of Bonn via a Web API that conforms to the OGC API Features specification. """

    links: Required[list["_ComponentsSchemasLink"]]
    """ Required property """


class GetResponse500(TypedDict, total=False):
    """Information about the exception: an error code plus an optional description."""

    code: Required[str]
    """ Required property """

    description: str


_COLLECTIONSCOLLECTIONIDGETRESPONSE200_CRS_DEFAULT = ["http://www.opengis.net/def/crs/OGC/1.3/CRS84"]
""" Default value of the field path 'CollectionsCollectionidGetResponse200 crs' """


_COLLECTIONSCOLLECTIONIDGETRESPONSE200_EXTENT_SPATIAL_CRS_DEFAULT = (
    "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
)
""" Default value of the field path 'CollectionsCollectionidGetResponse200 extent spatial crs' """


_COLLECTIONSCOLLECTIONIDGETRESPONSE200_EXTENT_TEMPORAL_TRS_DEFAULT = (
    "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
)
""" Default value of the field path 'CollectionsCollectionidGetResponse200 extent temporal trs' """


_COLLECTIONSCOLLECTIONIDGETRESPONSE200_ITEMTYPE_DEFAULT = "feature"
""" Default value of the field path 'CollectionsCollectionidGetResponse200 itemType' """


_COLLECTIONSCOLLECTIONIDITEMSGETQUERYLIMIT_DEFAULT = 10
""" Default value of the field path 'CollectionsCollectionidItemsGetQueryLimit' """


_COMPONENTS_SCHEMAS_COLLECTION_CRS_DEFAULT = ["http://www.opengis.net/def/crs/OGC/1.3/CRS84"]
""" Default value of the field path 'components schemas collection crs' """


_COMPONENTS_SCHEMAS_COLLECTION_ITEMTYPE_DEFAULT = "feature"
""" Default value of the field path 'components schemas collection itemType' """


_COMPONENTS_SCHEMAS_EXTENT_SPATIAL_CRS_DEFAULT = "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
""" Default value of the field path 'components schemas extent spatial crs' """


_COMPONENTS_SCHEMAS_EXTENT_TEMPORAL_TRS_DEFAULT = "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
""" Default value of the field path 'components schemas extent temporal trs' """


class _Collectionscollectionidgetresponse200Extent(TypedDict, total=False):
    """
    The extent of the features in the collection. In the Core only spatial and temporal
    extents are specified. Extensions may add additional members to represent other
    extents, for example, thermal or pressure ranges.
    """

    spatial: "_Collectionscollectionidgetresponse200ExtentSpatial"
    temporal: "_Collectionscollectionidgetresponse200ExtentTemporal"


class _Collectionscollectionidgetresponse200ExtentSpatial(TypedDict, total=False):
    """The spatial extent of the features in the collection."""

    bbox: list["_Collectionscollectionidgetresponse200ExtentSpatialBboxItem"]
    """
    One or more bounding boxes that describe the spatial extent of the dataset.
    In the Core only a single bounding box is supported. Extensions may support
    additional areas. If multiple areas are provided, the union of the bounding
    boxes describes the spatial extent.

    minItems: 1
    """

    crs: "_Collectionscollectionidgetresponse200ExtentSpatialCrs"


_Collectionscollectionidgetresponse200ExtentSpatialBboxItem = list[Union[int, float]]
"""
Each bounding box is provided as four or six numbers, depending on
whether the coordinate reference system includes a vertical axis
(height or depth):

* Lower left corner, coordinate axis 1
* Lower left corner, coordinate axis 2
* Minimum value, coordinate axis 3 (optional)
* Upper right corner, coordinate axis 1
* Upper right corner, coordinate axis 2
* Maximum value, coordinate axis 3 (optional)

The coordinate reference system of the values is WGS 84 longitude/latitude
(http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate
reference system is specified in `crs`.

For WGS 84 longitude/latitude the values are in most cases the sequence of
minimum longitude, minimum latitude, maximum longitude and maximum latitude.
However, in cases where the box spans the antimeridian the first value
(west-most box edge) is larger than the third value (east-most box edge).

If the vertical axis is included, the third and the sixth number are
the bottom and the top of the 3-dimensional bounding box.

If a feature has multiple spatial geometry properties, it is the decision of the
server whether only a single spatial geometry property is used to determine
the extent or all relevant geometries.
"""


_Collectionscollectionidgetresponse200ExtentSpatialCrs = Union[
    Literal["http://www.opengis.net/def/crs/OGC/1.3/CRS84"]
]
"""
Coordinate reference system of the coordinates in the spatial extent
(property `bbox`). The default reference system is WGS 84 longitude/latitude.
In the Core this is the only supported coordinate reference system.
Extensions may support additional coordinate reference systems and add
additional enum values.

default: http://www.opengis.net/def/crs/OGC/1.3/CRS84
"""
_COLLECTIONSCOLLECTIONIDGETRESPONSE200EXTENTSPATIALCRS_HTTP_COLON__SOLIDUS__SOLIDUS_WWW_FULL_STOP_OPENGIS_FULL_STOP_NET_SOLIDUS_DEF_SOLIDUS_CRS_SOLIDUS_OGC_SOLIDUS_1_FULL_STOP_3_SOLIDUS_CRS84: Literal[
    "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
] = "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
"""The values for the 'Coordinate reference system of the coordinates in the spatial extent' enum"""


class _Collectionscollectionidgetresponse200ExtentTemporal(TypedDict, total=False):
    """The temporal extent of the features in the collection."""

    interval: list["_Collectionscollectionidgetresponse200ExtentTemporalIntervalItem"]
    """
    One or more time intervals that describe the temporal extent of the dataset.
    The value `null` is supported and indicates an unbounded interval end.
    In the Core only a single time interval is supported. Extensions may support
    multiple intervals. If multiple intervals are provided, the union of the
    intervals describes the temporal extent.

    minItems: 1
    """

    trs: "_Collectionscollectionidgetresponse200ExtentTemporalTrs"


_Collectionscollectionidgetresponse200ExtentTemporalIntervalItem = list[
    "_Collectionscollectionidgetresponse200ExtentTemporalIntervalItemItem"
]
"""
Begin and end times of the time interval. The timestamps are in the
temporal coordinate reference system specified in `trs`. By default
this is the Gregorian calendar.

minItems: 2
maxItems: 2
"""


_Collectionscollectionidgetresponse200ExtentTemporalIntervalItemItem = str
"""
format: date-time
nullable: True
"""


_Collectionscollectionidgetresponse200ExtentTemporalTrs = Union[
    Literal["http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"]
]
"""
Coordinate reference system of the coordinates in the temporal extent
(property `interval`). The default reference system is the Gregorian calendar.
In the Core this is the only supported temporal coordinate reference system.
Extensions may support additional temporal coordinate reference systems and add
additional enum values.

default: http://www.opengis.net/def/uom/ISO-8601/0/Gregorian
"""
_COLLECTIONSCOLLECTIONIDGETRESPONSE200EXTENTTEMPORALTRS_HTTP_COLON__SOLIDUS__SOLIDUS_WWW_FULL_STOP_OPENGIS_FULL_STOP_NET_SOLIDUS_DEF_SOLIDUS_UOM_SOLIDUS_ISO_8601_SOLIDUS_0_SOLIDUS_GREGORIAN: Literal[
    "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
] = "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
"""The values for the 'Coordinate reference system of the coordinates in the temporal extent' enum"""


_Collectionscollectionidgetresponse200LinksItem = Any
""" WARNING: we get an schema without any type """


class _ComponentsSchemasCollection(TypedDict, total=False):
    id: Required[str]
    """
    identifier of the collection used, for example, in URIs

    example: address

    Required property
    """

    title: str
    """
    human readable title of the collection

    example: address
    """

    description: str
    """
    a description of the features in the collection

    example: An address.
    """

    links: Required[list["_ComponentsSchemasLink"]]
    """ Required property """

    extent: "_ComponentsSchemasExtent"
    itemType: str
    """
    indicator about the type of the items in the collection (the default value is 'feature').

    default: feature
    """

    crs: list[str]
    """
    the list of coordinate reference systems supported by the service

    default:
      - http://www.opengis.net/def/crs/OGC/1.3/CRS84
    """


class _ComponentsSchemasExtent(TypedDict, total=False):
    """
    The extent of the features in the collection. In the Core only spatial and temporal
    extents are specified. Extensions may add additional members to represent other
    extents, for example, thermal or pressure ranges.
    """

    spatial: "_ComponentsSchemasExtentSpatial"
    temporal: "_ComponentsSchemasExtentTemporal"


class _ComponentsSchemasExtentSpatial(TypedDict, total=False):
    """The spatial extent of the features in the collection."""

    bbox: list["_ComponentsSchemasExtentSpatialBboxItem"]
    """
    One or more bounding boxes that describe the spatial extent of the dataset.
    In the Core only a single bounding box is supported. Extensions may support
    additional areas. If multiple areas are provided, the union of the bounding
    boxes describes the spatial extent.

    minItems: 1
    """

    crs: "_ComponentsSchemasExtentSpatialCrs"


_ComponentsSchemasExtentSpatialBboxItem = list[Union[int, float]]
"""
Each bounding box is provided as four or six numbers, depending on
whether the coordinate reference system includes a vertical axis
(height or depth):

* Lower left corner, coordinate axis 1
* Lower left corner, coordinate axis 2
* Minimum value, coordinate axis 3 (optional)
* Upper right corner, coordinate axis 1
* Upper right corner, coordinate axis 2
* Maximum value, coordinate axis 3 (optional)

The coordinate reference system of the values is WGS 84 longitude/latitude
(http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate
reference system is specified in `crs`.

For WGS 84 longitude/latitude the values are in most cases the sequence of
minimum longitude, minimum latitude, maximum longitude and maximum latitude.
However, in cases where the box spans the antimeridian the first value
(west-most box edge) is larger than the third value (east-most box edge).

If the vertical axis is included, the third and the sixth number are
the bottom and the top of the 3-dimensional bounding box.

If a feature has multiple spatial geometry properties, it is the decision of the
server whether only a single spatial geometry property is used to determine
the extent or all relevant geometries.
"""


_ComponentsSchemasExtentSpatialCrs = Union[Literal["http://www.opengis.net/def/crs/OGC/1.3/CRS84"]]
"""
Coordinate reference system of the coordinates in the spatial extent
(property `bbox`). The default reference system is WGS 84 longitude/latitude.
In the Core this is the only supported coordinate reference system.
Extensions may support additional coordinate reference systems and add
additional enum values.

default: http://www.opengis.net/def/crs/OGC/1.3/CRS84
"""
_COMPONENTSSCHEMASEXTENTSPATIALCRS_HTTP_COLON__SOLIDUS__SOLIDUS_WWW_FULL_STOP_OPENGIS_FULL_STOP_NET_SOLIDUS_DEF_SOLIDUS_CRS_SOLIDUS_OGC_SOLIDUS_1_FULL_STOP_3_SOLIDUS_CRS84: Literal[
    "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
] = "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
"""The values for the 'Coordinate reference system of the coordinates in the spatial extent' enum"""


class _ComponentsSchemasExtentTemporal(TypedDict, total=False):
    """The temporal extent of the features in the collection."""

    interval: list["_ComponentsSchemasExtentTemporalIntervalItem"]
    """
    One or more time intervals that describe the temporal extent of the dataset.
    The value `null` is supported and indicates an unbounded interval end.
    In the Core only a single time interval is supported. Extensions may support
    multiple intervals. If multiple intervals are provided, the union of the
    intervals describes the temporal extent.

    minItems: 1
    """

    trs: "_ComponentsSchemasExtentTemporalTrs"


_ComponentsSchemasExtentTemporalIntervalItem = list["_ComponentsSchemasExtentTemporalIntervalItemItem"]
"""
Begin and end times of the time interval. The timestamps are in the
temporal coordinate reference system specified in `trs`. By default
this is the Gregorian calendar.

minItems: 2
maxItems: 2
"""


_ComponentsSchemasExtentTemporalIntervalItemItem = str
"""
format: date-time
nullable: True
"""


_ComponentsSchemasExtentTemporalTrs = Union[Literal["http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"]]
"""
Coordinate reference system of the coordinates in the temporal extent
(property `interval`). The default reference system is the Gregorian calendar.
In the Core this is the only supported temporal coordinate reference system.
Extensions may support additional temporal coordinate reference systems and add
additional enum values.

default: http://www.opengis.net/def/uom/ISO-8601/0/Gregorian
"""
_COMPONENTSSCHEMASEXTENTTEMPORALTRS_HTTP_COLON__SOLIDUS__SOLIDUS_WWW_FULL_STOP_OPENGIS_FULL_STOP_NET_SOLIDUS_DEF_SOLIDUS_UOM_SOLIDUS_ISO_8601_SOLIDUS_0_SOLIDUS_GREGORIAN: Literal[
    "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
] = "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
"""The values for the 'Coordinate reference system of the coordinates in the temporal extent' enum"""


class _ComponentsSchemasLink(TypedDict, total=False):
    href: Required[str]
    """
    example: http://data.example.com/buildings/123

    Required property
    """

    rel: str
    """ example: alternate """

    type: str
    """ example: application/geo+json """

    hreflang: str
    """ example: en """

    title: str
    """ example: Trierer Strasse 70, 53115 Bonn """

    length: int
