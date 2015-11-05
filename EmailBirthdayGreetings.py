__author__ = 'Yovin'
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText

message = '<html><head><title>Birthday Greetings</title></head><body><h1>Happy Birthday....{0}</h1><img src="http://cdn.wow.lk/var/gen/2014/newsletters/03-07/birthday_03.jpg" ' \
          'alt="Happy birthday - 5%" style="font-size: 10px; color:#d0d0d0; font-family: Arial, Helvetica, sans-serif; text-decoration: none;" width="660" height="208" />' \
          '</body></html>'.format('Yovin Lekamge')
def main():
    SendBirthdayGreetings(message, 'tharindu.prf@gmail.com', ['tharindu.prf@gmail.com', 'yovin99@hotmail.com'], 'Tharindu')

def SendBirthdayGreetings( message, emailReciever, recepients, emailRecieverName=None):
    # Create a Message object with the body text
    msg = MIMEMultipart()
    msg['From'] = 'yovinl@99x.lk' #reciption Email Adress
    msg['To'] = emailReciever
    msg['Cc'] = ', '.join(recepients)# Create a Message object with the body text
    msg['Subject'] = 'Happy Birthday... {0}!'.format(emailRecieverName)

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
        SENDER_EMAIL = 'yovinl@99x.lk'
        SENDER_PW = 'Gaara!23'
        mailserver.login(SENDER_EMAIL, SENDER_PW)
        # Send the email. Note we have to give sendmail() the message as a string
        # rather than a message object, so we need to do msg.as_string()
        mailserver.sendmail(SENDER_EMAIL, emailReciever ,msg.as_string())
        print "Greeting Successfully sent"
    except Exception, ex:
        exception = 'SMTP Exception:\n' + str(ex)
        print "Error Sending greetings {0}".format(exception)
    finally:
        mailserver.quit() # Close the connection


if __name__ == "__main__":
    main()

