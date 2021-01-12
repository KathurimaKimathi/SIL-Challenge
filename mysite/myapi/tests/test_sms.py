import africastalking
from django.test import TestCase
from decouple import config

USERNAME = config('AT_USERNAME')
API_KEY = config('AT_API_KEY')

africastalking.initialize(USERNAME, API_KEY)
token_service = africastalking.Token
service = africastalking.SMS


class TestSmsService(TestCase):
    def test_send(self):
        """Test Sending SMS"""
        res = service.send('Test message', ['+254705385894'])
        recipients = res['SMSMessageData']['Recipients']
        assert recipients[0]['status'] == 'Success'
