from urllib2 import Request, urlopen, URLError
import json
from calendar import monthrange
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

def birthdaycal(idnumber):
    #print(idnumber)
    year=int('19'+idnumber[:2])
    if(int(idnumber[2:5])>500):
        dmonth=int(idnumber[2:5])-500
    else:
        dmonth=int(idnumber[2:5])
    #print(dmonth)
    dayssum=0
    pmonthsum=0
    month=0
    days=[31,29,31,30,31,30,31,31,30,31,30,31]
    for i in days:
        
        dayssum+=i
        month+=1
        #print(dayssum)
        if(dmonth-dayssum<=0):
            #print(dmonth-pmonthsum)
            day=dmonth-pmonthsum
            month=month
            break
        
        pmonthsum=dayssum
     
    return(str(year)+'/'+str(month)+'/'+str(day))

request = Request('http://99xt.lk/services/api/Employees')

try:
	response = urlopen(request)
	string = response.read()
	
except URLError:
        f=open("Employees.json")
        string=f.read()
        #print 'No kittez. Got an error code:', e


obj=json.loads(string)
#cdate=datetime.datetime.now()
#currentDate=str(cdate.month)+'/'+str(cdate.day)
currentDate='10/24'
emailList=[]
bdayEmailList=[]
peoplewithbday=[]
t=[]
for people in obj:
    emailList.append(people['id']+'@99x.lk')
    #print(people['nic'])
    if(people['nic']==""):
        pass
    else:
        birthday=birthdaycal(people['nic'])
        t.append(birthday)
    #print(birthday)
    #print birthday[5:],currentDate
    if(birthday[5:]==currentDate):
        bdayEmailList.append(people['id']+'@99x.lk')
        peoplewithbday.append({'fname':people['firstName'],'lname':people['lastName'],'email':people['id']+'@99x.lk'})

emlist=['tharindur@99x.lk','raveenp@99x.lk','hansiniej@99x.lk']

def editmessage(url,name):
    message ="<!DOCTYPE html><html><head> <title></title><style>.pan_wrap{background: url(pan_checks.gif) repeat;position: relative;width: 250px;height: 230px;}.pan_frame{background: url(http://54.179.157.173/officebdaymanager/img/pan_frame3.png) no-repeat;overflow: hidden;position: absolute;top: 0;left: 0;width: 250px;height: 230px;}</style></head><body> <div> <table align='center' border='0' cellpadding='0' cellspacing='0' width='610'> <tr> <td> <table border='0' cellpadding='0' cellspacing='0' width='610'> <tr> <td align='center' bgcolor='#252525' style='border-bottom: 10px solid #EA6528; border-top: 5px solid #252525;'> <table border='0' cellpadding='0' cellspacing='0' width='600'> <tr> <td bgcolor='#252525'> <table border='0' cellpadding='0' cellspacing='0' width='100%'> <tr> <td><img height='150' src='http://54.179.157.173/officebdaymanager/img/1.png' width='600'></td></tr><tr> <td style='text-align: left;'> <div class='pan_wrap' style='margin:20px'> <img src='"+url+"' alt='panoramic' width='250px' height='230px'/> <div class='pan_frame'> &nbsp; </div></div></td><td style='text-align: right;'> <div style='text-align: right; margin-left: -350px; margin-right:20px;&gt;'> <img height='200' src='http://54.179.157.173/officebdaymanager/img/3.png' width='300'></div></td></tr><tr> <td align='center' style='font-size: 25px; color: #d0d0d0; font-family: Papyrus, fantasy; font-weight: 450; text-decoration: none;'> Wishing you hapiness and success in all your endeavous for the year ahead..</td></tr><tr> <td align='center' style='font-size: 60px; color: #d0d0d0; font-family: Papyrus, fantasy; font-weight: 600; text-decoration: none; padding-top: 20px;'> "+name+"</td></tr><tr> <td style='text-align:center;'> <img alt='Happy birthday - 5%' height='400' src='http://54.179.157.173/officebdaymanager/img/2.png' width='530' style='margin-top: -178px'></td></tr></table> </td></tr></table> </td></tr></table> </td></tr><tr> <td align='center' bgcolor='#252525' style='border-top: 15px solid #252525; border-bottom: 15px solid #252525;'> <table border='0' cellpadding='0' cellspacing='0' width='400'> <tr> <td align='center' style='font-size: 30px; color: #d0d0d0; font-family: Papyrus, fantasy; font-weight: 500; text-decoration: none;'> From all of us @</td><td><img height='35px' src='http://54.179.157.173/officebdaymanager/img/logo-white.png' width='130px'></td></tr></table> </td></tr><tr> <td></td></tr></table> </div></body></html></html>"
    return(message)


for emails in emlist:
    a=1
    name=emails[:-8]
    username=emails[:-7]
    url="http://54.179.157.173/officebdaymanager/img/"+username+".png"
    print(name,url)
    message=editmessage(url,name)
    SendBirthdayGreetings(message, emails, ['tharindu@gmail.com', 'yovin99@hotmail.com'], 'Tharindu')
    
