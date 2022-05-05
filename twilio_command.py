from service_request_log.abstract_service_call import (AbstractServiceCallCommand)
import requests
from typing import Union
from django.conf import settings
account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
baseURL = settings.TWILIO_BASE_URL


class TwilioCommand(AbstractServiceCallCommand):

    requests = requests
    response: Union[requests.Response, None] = None
    BASE_URL = baseURL
    HEADERS = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    AUTH = (account_sid, auth_token)

    def __init__(self, to: str, channel: str, FriendlyName: str):
        self.to = to
        self.channel = channel
        self.FriendlyName = FriendlyName

    def body(self) -> dict:
        return self._prepare_body()

    def _prepare_body(self) -> dict:
        body = {
            "FriendlyName": self.FriendlyName
        }
        return body

    def call_service(self) -> requests.Response:
        self.response = self.requests.post(
            self.BASE_URL,
            self.HEADERS,
            self.body(),
            self.AUTH,
        )
        return self.response

    def _get_response(self) -> dict:
        if self.response is None:
            raise Exception("response cannot be None")
        return self.response.json()

    def response_code(self) -> int:
        valid_response = self._get_response()
        return valid_response['status_code']

    def response_content(self) -> dict:
        response = self._get_response()
        return response.json()

    def result(self) -> str:
        twilio_response = self._get_response()
        response = twilio_response["account_sid"]
        return response

    @property
    def service(self) -> str:
        return "twilio"

    def url(self) -> str:
        return self.BASE_URL

    def valid_response(self) -> bool:
        twilio_response = self._get_response()
        if 'code' in twilio_response:
            return False
        return True
