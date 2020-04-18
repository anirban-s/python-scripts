import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Anirban Sarkar'
email['to'] = 'codingtutorial101@gmail.com'
email['subject'] = 'Test Email'

email.set_content(html.substitute({'name': 'Tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('codingtutorial101@gmail.com', 'password')
	smtp.send_message(email)
	print('All Good!!')