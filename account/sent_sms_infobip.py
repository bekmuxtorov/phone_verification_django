from django.conf import settings

from infobip_api_client.api_client import ApiClient, Configuration
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest
from infobip_api_client.model.sms_destination import SmsDestination
from infobip_api_client.model.sms_response import SmsResponse
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.exceptions import ApiException

import random


def create_code() -> int:
    return random.randint(1000, 9999)


BASE_URL = settings.INFOBIP_BASE_URL
API_KEY = settings.INFOBIP_API_KEY


def sent_sms_to_phone_number(phone_number: str):
    SENDER = "InfoSMS"
    RECIPIENT = phone_number
    code = create_code()
    MESSAGE_TEXT = f"Your verification PIN is: {code}"

    client_config = Configuration(
        host=BASE_URL,
        api_key={"APIKeyHeader": API_KEY},
        api_key_prefix={"APIKeyHeader": "App"},
    )

    api_client = ApiClient(client_config)

    sms_request = SmsAdvancedTextualRequest(
        messages=[
            SmsTextualMessage(
                destinations=[
                    SmsDestination(
                        to=RECIPIENT,
                    ),
                ],
                _from=SENDER,
                text=MESSAGE_TEXT,
            )
        ])

    api_instance = SendSmsApi(api_client)

    try:
        api_response: SmsResponse = api_instance.send_sms_message(
            sms_advanced_textual_request=sms_request)
        print(api_response)
        return code
    except ApiException as ex:
        print("Error occurred while trying to send SMS message.")
        return None
