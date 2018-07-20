import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient()
from_email = Email("sergiomonteirodev@gmail.com")
to_email = Email("sergiomonteirodev@gmail.com")
subject = "Certificado professor dedeco"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)