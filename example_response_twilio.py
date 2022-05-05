correct_response_get_twilio_sid = {
    "default_template_sid": None,
    "tts_name": None,
    "status_code": 200,
    "psd2_enabled": False,
    "do_not_share_warning_enabled": False,
    "mailer_sid": None,
    "friendly_name": "My Verify Service",
    "url": "https://verify.twilio.com/v2/Services/VA3e5025034fee62a171f354ba35a9fc28",
    "account_sid": "ACb62b6a2c88aec5d2c86a809c8c988499",
    "date_updated": "2022-04-13T10:39:57Z",
    "totp": {
        "time_step": 30,
        "skew": 1,
        "code_length": 6,
        "issuer": "My Verify Service",
    },
    "code_length": 6,
    "custom_code_enabled": False,
    "sid": "VA3e5025034fee62a171f354ba35a9fc28",
    "push": {
        "apn_credential_sid": None,
        "include_date": True,
        "fcm_credential_sid": None,
    },
    "date_created": "2022-04-13T10:39:57Z",
    "dtmf_input_required": True,
    "skip_sms_to_landlines": True,
    "lookup_enabled": True,
    "links": {
        "verification_checks": "https://verify.twilio.com/v2/Services/VA3e5025034fee62a171f354ba35a9fc28/VerificationCheck",
        "rate_limits": "https://verify.twilio.com/v2/Services/VA3e5025034fee62a171f354ba35a9fc28/RateLimits",
        "entities": "https://verify.twilio.com/v2/Services/VA3e5025034fee62a171f354ba35a9fc28/Entities",
        "access_tokens": "https://verify.twilio.com/v2/Services/VA3e5025034fee62a171f354ba35a9fc28/AccessTokens",
        "verifications": "https://verify.twilio.com/v2/Services/VA3e5025034fee62a171f354ba35a9fc28/Verifications",
        "webhooks": "https://verify.twilio.com/v2/Services/VA3e5025034fee62a171f354ba35a9fc28/Webhooks",
        "messaging_configurations": "https://verify.twilio.com/v2/Services/VA3e5025034fee62a171f354ba35a9fc28/MessagingConfigurations",
    },
}

correct_response_send_sms = {
    "status": "pending",
    "payee": None,
    "date_updated": "2022-04-13T13:14:56Z",
    "send_code_attempts": [
        {
            "attempt_sid": "VL871e69f7bd0ee3637fc5caec507a8c70",
            "channel": "sms",
            "time": "2022-04-13T13:14:56.433Z",
        }
    ],
    "account_sid": "ACb62b6a2c88aec5d2c86a809c8c988499",
    "to": "+34666027635",
    "amount": None,
    "valid": False,
    "lookup": {
        "carrier": {
            "mobile_country_code": "214",
            "type": "mobile",
            "error_code": None,
            "mobile_network_code": "01",
            "name": "VODAFONE ESPAÑA",
        }
    },
    "url": "https://verify.twilio.com/v2/Services/VAde0a816eec2810beec61bf70e07c400d/Verifications/VEd806afc437be86779ac53c1a11cffb37",
    "sid": "VEd806afc437be86779ac53c1a11cffb37",
    "date_created": "2022-04-13T13:14:56Z",
    "service_sid": "VAde0a816eec2810beec61bf70e07c400d",
    "channel": "sms",
}

fail_response_send_sms = {
    "status": "fail",
    "payee": None,
    "date_updated": "2022-04-13T13:14:56Z",
    "send_code_attempts": [
        {
            "attempt_sid": "VL871e69f7bd0ee3637fc5caec507a8c70",
            "channel": "sms",
            "time": "2022-04-13T13:14:56.433Z",
        }
    ],
    "account_sid": "ACb62b6a2c88aec5d2c86a809c8c988499",
    "to": "+34666027635",
    "amount": None,
    "valid": False,
    "lookup": {
        "carrier": {
            "mobile_country_code": "214",
            "type": "mobile",
            "error_code": None,
            "mobile_network_code": "01",
            "name": "VODAFONE ESPAÑA",
        }
    },
    "url": "https://verify.twilio.com/v2/Services/VAde0a816eec2810beec61bf70e07c400d/Verifications/VEd806afc437be86779ac53c1a11cffb37",
    "sid": "VEd111afc111be11111ac53c1a11cffb37",
    "date_created": "2022-04-13T13:14:56Z",
    "service_sid": "VAde0a816eec2810beec61bf70e07c400d",
    "channel": "sms",
}


fail_response_get_twilio_sid = {
    "code": 20003,
    "detail": "",
    "message": "Authenticate",
    "more_info": "https://www.twilio.com/docs/errors/20003",
    "status": 401,
}
