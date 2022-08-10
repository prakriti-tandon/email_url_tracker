import smtplib
#import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS=''#insert your email id here - not disclosed mine for privacy
EMAIL_PASSWORD=''#insert authorisation key for your email id



msg=EmailMessage()
msg['Subject']='CHECK OUT THIS URL!'
msg['From']=EMAIL_ADDRESS
msg['To']='testprogram130@gmail.com'

#HTML email body with the URL to be clicked
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <p>This is a link for you!<br>
              <a href="http://127.0.0.1:5000/">link</a> #URL
        </p>
    </body>
</html>
""",subtype='html')

#logging into user's email id and sending the email
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
