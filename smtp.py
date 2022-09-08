import email
import json
inbound = open("/home/baremetal/Dev Ops/all_tokens.json")
TOKENS =  json.load(inbound)

USERNAME = TOKENS["outlook.com mail"]
AUTH = TOKENS["outlook.com pass"]
import smtplib 

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sms_gateway = 'hazmatlatif@gmail.com'
smtp = "smtp-mail.outlook.com" 
port = 587

# Starts and keeps active an smpt server with "with" keyword

with smtplib.SMTP(smtp,port) as server:
    server.starttls()
    server.login(USERNAME,AUTH)

    # MIME module to structure message. Sets the From,To,Subject and Body
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    msg['Subject'] = "First Mail Script\n"
    body = "Hello World\n"

    # Attach body(can be and html-content) to multipart headers.
    msg.attach(MIMEText(body, 'plain'))
    
    # Transforms multipart to string 
    sms = msg.as_string()
    
    # Forwards message with server
    server.sendmail(email,sms_gateway,sms)

# Another way of going about the problem

'''
with smtplib.SMTP('smtp-mail.outlook.com',587) as connection:
    connection.ehlo()
    connection.starttls()

    connection = smtplib.SMTP('smtp.mail.yahoo.com',25)
    connection.starttls()
    connection.login(user = my_mail, password = my_pass)
    connection.sendmail(my_mail,"hazmatlatif@gmail.com",msg='Subject:Remade \n\n!')
    connection.close()
'''