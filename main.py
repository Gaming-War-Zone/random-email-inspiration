import random
import os, sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_quote(recipient_email='benedicttshivhase@gmail.com'):
    if len(sys.argv) == 2:
        recipient_email = sys.argv[-1]
    quote = get_quote()
    print(recipient_email)
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    smtp_login = os.getenv('SMTP_LOGIN')
    password = os.getenv('SMTP_PASSWORD')
    message = MIMEMultipart("alternative")
    message["Subject"] = "Inspirational Quote"
    message["From"] = smtp_login
    message["To"] = recipient_email
    html = quote
    quote_ = MIMEText(html, "html")
    message.attach(quote_)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, int(smtp_port), context=context) as server:
        server.login(smtp_login, password)
        server.sendmail(
            smtp_login, recipient_email, message.as_string()
        )


def get_quote():
    with open('quotes.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    res_dct = {lines[i]: lines[i + 1] for i in range(0, len(lines), 2)}
    randon_num = random.randint(0, len(res_dct))
    quote = list(res_dct)[randon_num]
    author = res_dct.get(quote).replace('--', '')
    quote = quote.strip('\n')
    quote = " -".join([quote, author])
    html = f"""\
        <html>
          <body>
            <h1>Hello, here's a quote to get your day started</h1>
            <p><b>{quote}</b></p>
          </body>
        </html>
        """
    return html

if __name__ == "__main__":
    send_quote()

