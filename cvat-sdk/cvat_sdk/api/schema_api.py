"""
    CVAT REST API

    REST API for Computer Vision Annotation Tool (CVAT)  # noqa: E501

    The version of the OpenAPI document: alpha (2.0)
    Contact: support@cvat.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations

import re  # noqa: F401
import typing
from typing import TYPE_CHECKING

import urllib3

from cvat_sdk.api_client import ApiClient
from cvat_sdk.api_client import Endpoint as _Endpoint
from cvat_sdk.model_utils import date, datetime, file_type, none_type  # noqa: F401

if TYPE_CHECKING:
    # Enable introspection. Can't work normally due to cyclic imports
    from cvat_sdk.apis import *
    from cvat_sdk.models import *


class SchemaApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.retrieve_endpoint = _Endpoint(
            settings={
                "response_schema": (
                    {str: (bool, date, datetime, dict, float, int, list, str, none_type)},
                ),
                "auth": ["SignatureAuthentication", "basicAuth", "cookieAuth", "tokenAuth"],
                "endpoint_path": "/api/schema/",
                "operation_id": "retrieve",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "x_organization",
                    "lang",
                    "org",
                    "org_id",
                    "scheme",
                ],
                "required": [],
                "nullable": [],
                "enum": [
                    "lang",
                    "scheme",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("lang",): {
                        "AF": "af",
                        "AR": "ar",
                        "AR-DZ": "ar-dz",
                        "AST": "ast",
                        "AZ": "az",
                        "BE": "be",
                        "BG": "bg",
                        "BN": "bn",
                        "BR": "br",
                        "BS": "bs",
                        "CA": "ca",
                        "CS": "cs",
                        "CY": "cy",
                        "DA": "da",
                        "DE": "de",
                        "DSB": "dsb",
                        "EL": "el",
                        "EN": "en",
                        "EN-AU": "en-au",
                        "EN-GB": "en-gb",
                        "EO": "eo",
                        "ES": "es",
                        "ES-AR": "es-ar",
                        "ES-CO": "es-co",
                        "ES-MX": "es-mx",
                        "ES-NI": "es-ni",
                        "ES-VE": "es-ve",
                        "ET": "et",
                        "EU": "eu",
                        "FA": "fa",
                        "FI": "fi",
                        "FR": "fr",
                        "FY": "fy",
                        "GA": "ga",
                        "GD": "gd",
                        "GL": "gl",
                        "HE": "he",
                        "HI": "hi",
                        "HR": "hr",
                        "HSB": "hsb",
                        "HU": "hu",
                        "HY": "hy",
                        "IA": "ia",
                        "ID": "id",
                        "IG": "ig",
                        "IO": "io",
                        "IS": "is",
                        "IT": "it",
                        "JA": "ja",
                        "KA": "ka",
                        "KAB": "kab",
                        "KK": "kk",
                        "KM": "km",
                        "KN": "kn",
                        "KO": "ko",
                        "KY": "ky",
                        "LB": "lb",
                        "LT": "lt",
                        "LV": "lv",
                        "MK": "mk",
                        "ML": "ml",
                        "MN": "mn",
                        "MR": "mr",
                        "MY": "my",
                        "NB": "nb",
                        "NE": "ne",
                        "NL": "nl",
                        "NN": "nn",
                        "OS": "os",
                        "PA": "pa",
                        "PL": "pl",
                        "PT": "pt",
                        "PT-BR": "pt-br",
                        "RO": "ro",
                        "RU": "ru",
                        "SK": "sk",
                        "SL": "sl",
                        "SQ": "sq",
                        "SR": "sr",
                        "SR-LATN": "sr-latn",
                        "SV": "sv",
                        "SW": "sw",
                        "TA": "ta",
                        "TE": "te",
                        "TG": "tg",
                        "TH": "th",
                        "TK": "tk",
                        "TR": "tr",
                        "TT": "tt",
                        "UDM": "udm",
                        "UK": "uk",
                        "UR": "ur",
                        "UZ": "uz",
                        "VI": "vi",
                        "ZH-HANS": "zh-hans",
                        "ZH-HANT": "zh-hant",
                    },
                    ("scheme",): {"JSON": "json", "YAML": "yaml"},
                },
                "openapi_types": {
                    "x_organization": (str,),
                    "lang": (str,),
                    "org": (str,),
                    "org_id": (int,),
                    "scheme": (str,),
                },
                "attribute_map": {
                    "x_organization": "X-Organization",
                    "lang": "lang",
                    "org": "org",
                    "org_id": "org_id",
                    "scheme": "scheme",
                },
                "location_map": {
                    "x_organization": "header",
                    "lang": "query",
                    "org": "query",
                    "org_id": "query",
                    "scheme": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": [
                    "application/vnd.oai.openapi",
                    "application/yaml",
                    "application/vnd.oai.openapi+json",
                    "application/json",
                ],
                "content_type": [],
            },
            api_client=api_client,
        )

    def retrieve(
        self,
        *,
        _parse_response: bool = True,
        _request_timeout: typing.Union[int, float, tuple] = None,
        _validate_inputs: bool = True,
        _validate_outputs: bool = True,
        _check_status: bool = True,
        _spec_property_naming: bool = False,
        _content_type: typing.Optional[str] = None,
        _host_index: typing.Optional[int] = None,
        _request_auths: typing.Optional[typing.List] = None,
        _async_call: bool = False,
        **kwargs,
    ) -> typing.Tuple[
        typing.Optional[typing.Dict[str, typing.Union[typing.Any, none_type]]], urllib3.HTTPResponse
    ]:
        """retrieve  # noqa: E501

        OpenApi3 schema for this API. Format can be selected via content negotiation.  - YAML: application/vnd.oai.openapi - JSON: application/vnd.oai.openapi+json  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass _async_call=True

        >>> thread = api.retrieve(_async_call=True)
        >>> result = thread.get()


        Keyword Args:
            x_organization (str): [optional]
            lang (str): [optional]
            org (str): Organization unique slug. [optional]
            org_id (int): Organization identifier. [optional]
            scheme (str): [optional]
            _parse_response (bool): if False, the response data will not be parsed,
                None is returned for data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _validate_inputs (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _validate_outputs (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _check_status (bool): whether to check response status
                for being positive or not.
                Default is True
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            _async_call (bool): execute request asynchronously

        Returns:
            ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, HTTPResponse)
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["_async_call"] = _async_call
        kwargs["_parse_response"] = _parse_response
        kwargs["_request_timeout"] = _request_timeout
        kwargs["_validate_inputs"] = _validate_inputs
        kwargs["_validate_outputs"] = _validate_outputs
        kwargs["_check_status"] = _check_status
        kwargs["_spec_property_naming"] = _spec_property_naming
        kwargs["_content_type"] = _content_type
        kwargs["_host_index"] = _host_index
        kwargs["_request_auths"] = _request_auths
        return self.retrieve_endpoint.call_with_http_info(**kwargs)
