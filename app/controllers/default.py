from app import app
from flask import render_template, request
import sendgrid, os
from sendgrid.helpers.mail import *


@app.route("/", methods=['GET', 'POST'])
def index():
     if request.method == 'POST':
        emails = request.form['emails']

        sg = sendgrid.SendGridAPIClient()
        from_email = Email("sergiomonteirodev@gmail.com")
        to_email = Email(emails)
        subject = "Certificado professor dedeco"
        content = Content("text/plain", "and easy to do anywhere, even with Python")
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)
    return render_template("index.html")
    