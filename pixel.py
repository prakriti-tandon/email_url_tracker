import smtplib
#import imghdr
from email.message import EmailMessage


EMAIL_ADDRESS=''#insert your email id here - not disclosed mine for privacy
EMAIL_PASSWORD=''#insert authorisation key for your email id



msg=EmailMessage()
msg['Subject']='CHECK OUT THIS URL!'
msg['From']=EMAIL_ADDRESS
msg['To']='testprogram130@gmail.com'

#HTML email body 
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <p>Hey! How are you<br>
        </p>
        <img src="http://127.0.0.1:5000/pixel.gif" width="1" height="1"/> #link to a tracking pixel located in a web server created by website_pixel.py
    </body>
</html>
""",subtype='html')

#logging into user's email account and send this email
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
