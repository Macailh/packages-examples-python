import os
from twilio.rest import Client

sid = os.environ.get("TWILIO_ACCOUNT_SID")
token = os.environ.get("TWILIO_AUTH_TOKEN")
phone = os.environ.get("TWILIO_PHONE_NUMBER")
client = Client(sid, token)

mensaje = client.messages.create(
    body="Hola karnal, que hace? nada o ke ase xd .....",
    from_=phone,
    to="+523861207715"
)
