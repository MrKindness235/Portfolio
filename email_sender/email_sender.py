#!/usr/bin/env python3

import email.message import EmailMessage
from app2 import password

# go over to our gmail account and setup 3 factor authentication
# generate app password
# create a function to send the mail

email_sender = 'exampleemail@gmail.com'
email_password = password

email_receiver = ''

subject = "Never forget."
body = """
Aslong as we remember them, they stay with us-- forever.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)
