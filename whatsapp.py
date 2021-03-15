import smtplib
from email.message import EmailMessage

def emailalert(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = 'jha36binayak@gmail.com'
    msg['from'] = user
    password = 'uwvoqfkgbkrvmelp'

    server = smtplib.SMTP("smtp.gmail.com", 587) 
    server.starttls()
    server.login(user,password) 
    server.send_message(msg)

    server.quit()  

if __name__=='__main__':
    emailalert("Hey","Just a test message from python",' +9779803096555@sms.ncell.com.np')