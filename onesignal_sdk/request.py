import logging
from typing import Any, Dict

import requests

from .error import OneSignalHTTPError
from .response import OneSignalResponse

logger = logging.getLogger(__name__)


def _build_request_kwargs(
    token: str = None, payload: Dict[str, Any] = None, params: Dict[str, Any] = None
) -> Dict[str, Any]:
    request_kwargs = {}
    if token is not None:
        request_kwargs["headers"] = {"Authorization": "Basic {0}".format(token)}
    if payload is not None:
        request_kwargs["json"] = payload
    if params is not None:
        request_kwargs["params"] = params
    return request_kwargs


def _handle_response(
    response: requests.Response, silence_error=True
) -> OneSignalResponse:
    """Given an requests.Response either raise an Exception or return final Response object."""
    if response.status_code >= 300:
        logger.error(
            f"Onesignal error on {response.url}, reason {response.reason}",
            response.json(),
        )
        if not silence_error:
            raise OneSignalHTTPError(response)

    return OneSignalResponse(response)


def basic_auth_request(
    method: str,
    url: str,
    token: str = None,
    payload: Dict[str, Any] = None,
    params: Dict[str, Any] = None,
    silence_error=True,
) -> OneSignalResponse:
    """Make a request using basic authorization."""
    request_kwargs = _build_request_kwargs(token, payload, params)
    return _handle_response(
        requests.request(method, url, **request_kwargs), silence_error
    )
