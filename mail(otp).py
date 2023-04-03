import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,otp):
    server=smtplib.SMTP('smtp.gmail,com',465)
    server.starttls()
    server.login('jahnavipasupuleti1302@gmail.com','ulnxzylfqjwfsaak')
    msg=EmailMessage()
    msg['From']='jahnavipasupuleti1302@gmail.com''
    msg['Subject']='Account Sign up OTP'
    msg['To']=to
    body=f 'our one time otp for registration is {otp}'
    msg.set_content(body)
    server.send_message(msg)
    server.close()
