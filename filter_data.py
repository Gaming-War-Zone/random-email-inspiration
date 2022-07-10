import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = os.getenv('SMTP_LOGIN')
receiver_email = "comedysessions@gmail.com"
password = os.getenv('SMTP_PASSWORD')

message = MIMEMultipart("alternative")
message["Subject"] = "Inspirational Quote"
message["From"] = sender_email
message["To"] = receiver_email

html = """\
<html>
  <body>
    <h1>
        Hello, here's an quote to get your day started
    </h1>
    <p><b>quote</b></p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(os.getenv('SMTP_SERVER'), 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )