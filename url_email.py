import smtplib
#import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS='testprogram130@gmail.com'
EMAIL_PASSWORD='zqbxybwezdjnuhon'



msg=EmailMessage()
msg['Subject']='CHECK OUT THIS URL!'
msg['From']=EMAIL_ADDRESS
msg['To']='testprogram130@gmail.com'
#msg.set_content("Click on this url")

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <p>This is a link for you!<br>
              <a href="http://127.0.0.1:5000/">link</a>
        </p>
    </body>
</html>
""",subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
