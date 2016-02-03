#!/usr/bin/env python
from urllib2 import Request, urlopen, URLError
import json
from calendar import monthrange
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Birthdaycal import *
from Email import *

request = Request('http://99xt.lk/services/api/Employees')
file=open('message.config')

print(file.readlines())


try:
	response = urlopen(request)
	string = response.read()
	
except URLError:
        f=open("Employees.json")
        string=f.read()
        #print 'No kittez. Got an error code:', e


obj=json.loads(string)
cdate=datetime.datetime.now()
#currentDate=str(cdate.month)+'/'+str(cdate.day) #getting the current date
currentDate='7/7'
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

emlist=bdayEmailList



def editmessage(url,name):
    message ="""<!DOCTYPE html><html><head> <title></title><style>.pan_wrap{position: relative;max-width: 300px;max-height: 290px;width: 250px;height: 230px;}
                .pan_frame{overflow: hidden;position: absolute;top: 0;left: 0;max-width: 300px;max-height: 290px;width: 250px;height: 230px;}</style>
                </head><body> <div> <table align='center' border='0' cellpadding='0' cellspacing='0' width='610'> <tr> <td>
                <table border='0' cellpadding='0' cellspacing='0' width='610'> <tr>
                <td align='center' bgcolor='#252525' style='border-bottom: 10px solid #EA6528; border-top: 5px solid #252525;'>
                <table border='0' cellpadding='0' cellspacing='0' width='600'> <tr> <td bgcolor='#252525'> <table border='0' cellpadding='0' cellspacing='0' width='100%'>
                <tr> <td><img height='150' src='http://54.179.157.173/officebdaymanager/img/1.png' width='600'></td></tr><tr> <td style='text-align: center;'>
                <div class='pan_wrap' style='margin:20px'> <img src='"+url+"' alt='panoramic' width='250px' height='250px'/> <div class='pan_frame'> &nbsp;
                </div></div></td></tr><tr> <td align='center' style='font-size: 25px; color: #d0d0d0; font-family: Papyrus, fantasy; font-weight: 450; text-decoration: none;'>
                Wishing you happiness and success in all your endeavous for the year ahead..
                </td></tr><tr> <td style='text-align:center; font-size: 60px; color: #d0d0d0; font-family: Papyrus, fantasy; font-weight: 600; text-decoration: none;
                padding-top: 20px;'> "+name.title()+"</td></tr><tr> <td style='text-align:center;'>
                <img alt='Happy birthday - 5%' height='400' src='http://54.179.157.173/officebdaymanager/img/2.png' width='530' style='margin-top: -150px'>
                </td></tr></table> </td></tr></table> </td></tr></table> </td></tr><tr>
                <td align='center' bgcolor='#252525' style='border-top: 15px solid #252525; border-bottom: 15px solid #252525;'>
                <table border='0' cellpadding='0' cellspacing='0' width='400'> <tr>
                <td align='center' style='font-size: 30px; color: #d0d0d0; font-family: Papyrus, fantasy; font-weight: 500; text-decoration: none;'>
                From all of us @</td><td><img height='30px' src='http://54.179.157.173/officebdaymanager/img/logo-white.png' width='120px'></td></tr>
                </table> </td></tr><tr> <td></td></tr></table> </div></body></html></html>"""
    return(message)


for emails in emlist:
    name=emails[:-8]
    username=emails[:-7]
    url="http://54.179.157.173/officebdaymanager/img/"+username+".png"
    print(name,url)
    message=editmessage(url,name.title())
    SendBirthdayGreetings(message, emails,['tharindu.prf@gmail.com'] ,username[:-1].title())
   
    
