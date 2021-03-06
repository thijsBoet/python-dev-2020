import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import os

# read html file
html = Template(Path('index.htm').read_text())

# setup email Object
email = EmailMessage()
email['from'] = 'Matthijs Boet'
email['to'] = os.environ.get('gmail_email')
email['subject'] = 'You won, congrats!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

# login and send email Object
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(os.environ.get('gmail_email'), os.environ.get('gmail_password'))
    smtp.send_message(email)
    print('mail send')
    smtp.close()
