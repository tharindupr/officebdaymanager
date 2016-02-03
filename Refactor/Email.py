#!/usr/bin/env python
from urllib2 import Request, urlopen, URLError
import json
from calendar import monthrange
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

__name__='Email'

config = {}
with open("app.config") as f:
    for line in f:
       (key, val) = line.split('=')
       config[key] = val.strip()

def SendBirthdayGreetings( message, emailReciever, recepients, emailRecieverName=None):
    # Create a Message object with the body text
    msg = MIMEMultipart()
    msg['From'] = config['SENDER_EMAIL'] #reciption Email Adress
    msg['To'] = emailReciever
    msg['Cc'] = ', '.join(recepients)# Create a Message object with the body text
    msg['Subject'] = config['SUBJECT'].format(emailRecieverName)

    try:
        msg.attach(MIMEText(message, 'html'))
        #mail server configurations
        mailserver = smtplib.SMTP('mail.99xtechnology.com')
        # identify ourselves to smtp office 365 client
        mailserver.ehlo()
        # secure our email with tls encryption
        mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        #add proper user credintials of the sender
        SENDER_EMAIL = config['SENDER_EMAIL']
        SENDER_PW = config['SENDER_PW']
        mailserver.login(SENDER_EMAIL, SENDER_PW)
        # Send the email. Note we have to give sendmail() the message as a string
        # rather than a message object, so we need to do msg.as_string()
        mailserver.sendmail(SENDER_EMAIL, emailReciever ,msg.as_string())
        mailserver.sendmail(SENDER_EMAIL, recepients ,msg.as_string())
        print "Greeting Successfully sent"
    except Exception, ex:
        exception = 'SMTP Exception:\n' + str(ex)
        print "Error Sending greetings {0}".format(exception)
    finally:
        mailserver.quit() # Close the connection
