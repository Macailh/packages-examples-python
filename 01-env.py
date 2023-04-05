import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

apikey = os.environ.get("SENDGRID_API_KEY")
email = os.environ.get("SENDGRID_EMAIL")

mensaje = Mail(
    from_email=email,
    to_emails="adrian.german4485@alumnos.udg.mx",
    subject="Prueba",
    html_content="<strong>Esto es una prueba</strong>"
)

try:
    apikey = os.environ.get("SENDGRID_API_KEY")
    sg = SendGridAPIClient(apikey)
    respuesta = sg.send(mensaje)

    print(respuesta.status_code, respuesta.body, respuesta.headers)
except Exception as e:
    print(e)
