#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


class Notifier:
   def __init__(self, email, password):
      self.email = email
      self.password = password

   def deliver(self, subject, emailBody = None):
      msg = MIMEMultipart()

      msg['From'] = self.email
      msg['To'] = self.email
      msg['Subject'] = subject

      msg.attach(MIMEText(emailBody))

      mailServer = smtplib.SMTP("smtp.gmail.com", 587)
      mailServer.ehlo()
      mailServer.starttls()
      mailServer.ehlo()
      mailServer.login(self.email, self.password)
      mailServer.sendmail(self.email, self.email, msg.as_string())
      # Should be mailServer.quit(), but that crashes...
      mailServer.close()