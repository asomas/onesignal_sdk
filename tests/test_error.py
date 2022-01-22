from onesignal_sdk.error import OneSignalHTTPError

from .mocks import MockRequestsResponse


class TestOneSignalHTTPError:
    def test_sets_message_when_response_contains_errors(self):
        response = MockRequestsResponse(
            400,
            {
                "errors": [
                    "Something went wrong with your request",
                    "Dont show this error",
                ]
            },
        )
        error = OneSignalHTTPError(response)
        assert error.message == "Something went wrong with your request"
        assert error.status_code == 400

    def test_uses_default_message_for_malformed_response(self):
        response = MockRequestsResponse(500, {})
        error = OneSignalHTTPError(response)
        assert error.message == "Unexpected http status code 500."
        assert error.status_code == 500
