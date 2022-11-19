import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='19cs079@kcgcollege.com',
    to_emails='varboroo@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

sg = SendGridAPIClient(os.environ.get('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'))
response = sg.send(message)
print(response.status_code)
print(response.body)
print(response.headers)
