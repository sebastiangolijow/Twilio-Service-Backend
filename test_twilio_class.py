from smschecker.twilio_command import TwilioCommand
import json
import requests
from src.service.smschecker.tests.test_services.example_response_twilio import (
    correct_response_get_twilio_sid,
)
from unittest.mock import MagicMock


class TestTwilio:
    def test_init(self):
        twilio_init = TwilioCommand(
            to='+34666027635', 
            channel='sms',
            FriendlyName='My First Class'
            )
        assert isinstance(twilio_init, TwilioCommand)

    def test_body(self):
        twilio_body = TwilioCommand(
            to='+34666027635', 
            channel='sms',
            FriendlyName='My First Class'
            )
        assert isinstance(twilio_body, TwilioCommand)

    def test_call_service(self):
        request_mock_response = requests.Response()
        request_mock_response.status_code = 200
        request_mock_response._content = bytes(
            json.dumps(correct_response_get_twilio_sid), "utf-8"
        )
        request_mock = MagicMock()
        request_mock.post.return_value = request_mock_response
        twilio_service = TwilioCommand(
            to='+34666027635', 
            channel='sms',
            FriendlyName='My First Class'
            )
        twilio_service.requests = request_mock
        service_response = twilio_service.call_service()
        assert service_response.json()['friendly_name'] == 'My Verify Service'
        assert isinstance(service_response.json()['friendly_name'], str)

    def test_response_code(self):
        request_mock_response = requests.Response()
        request_mock_response.status_code = 200
        request_mock_response._content = bytes(
            json.dumps(correct_response_get_twilio_sid), "utf-8"
        )
        request_mock = MagicMock()
        request_mock.post.return_value = request_mock_response
        twilio_service = TwilioCommand(
            to='+34666027635', 
            channel='sms',
            FriendlyName='My First Class'
            )
        twilio_service.requests = request_mock
        twilio_service.call_service()
        service_response_code = twilio_service.response_code()
        assert isinstance(service_response_code, int)

    def test_result(self):
        request_mock_response = requests.Response()
        request_mock_response.status_code = 200
        request_mock_response._content = bytes(
            json.dumps(correct_response_get_twilio_sid), "utf-8"
        )
        request_mock = MagicMock()
        request_mock.post.return_value = request_mock_response
        twilio_service = TwilioCommand(
            to='+34666027635', 
            channel='sms',
            FriendlyName='My First Class'
            )
        twilio_service.requests = request_mock
        twilio_service.call_service()
        service_response_sid = twilio_service.result()
        assert isinstance(service_response_sid, str)

    def test_url(self):
        request_mock_response = requests.Response()
        request_mock_response.status_code = 200
        request_mock_response._content = bytes(
            json.dumps(correct_response_get_twilio_sid), "utf-8"
        )
        request_mock = MagicMock()
        request_mock.post.return_value = request_mock_response
        twilio_service = TwilioCommand(
            to='+34666027635', 
            channel='sms',
            FriendlyName='My First Class'
            )
        twilio_service.requests = request_mock
        twilio_service.call_service()
        service_response_url = twilio_service.url()
        assert isinstance(service_response_url, str)


    def test_valid_response(self):
        request_mock_response = requests.Response()
        request_mock_response.status_code = 200
        request_mock_response._content = bytes(
            json.dumps(correct_response_get_twilio_sid), "utf-8"
        )
        request_mock = MagicMock()
        request_mock.post.return_value = request_mock_response
        twilio_service = TwilioCommand(
            to='+34666027635', 
            channel='sms',
            FriendlyName='My First Class'
            )
        twilio_service.requests = request_mock
        twilio_service.call_service()
        service_valid_response = twilio_service.valid_response()
        assert isinstance(service_valid_response, bool)
