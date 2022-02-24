from twilio.rest import Client
TWILIO_SID = 'ACb0f9c187be5d5808e409d292040b2ddb'
TWILIO_AUTH_TOKEN = 'bfe14eb0057be1e56795ed640e11ad8f'


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            messaging_service_sid='MGd866751ce2262055d0dd71dbb35ca0b2',
            body=message,
            to='+40757739687'
        )
        print(message.status)