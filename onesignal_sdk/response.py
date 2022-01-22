import requests


class OneSignalResponse:
    """
    Designates a successful response from OneSignal with body.
    """

    def __init__(self, response: requests.Response):
        self.http_response = response
        self.status_code = response.status_code
        self.body = response.json()
