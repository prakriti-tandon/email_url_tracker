# email_url_tracker
Project sends an email and checks if a url in the email was clicked or not 

SECTION 1: There is a url in an email and when the user clicks on the url, a notification is printed on the command terminal 

website.py - running this file creates a web server using Flask. If the server recieves a GET request, it triggers an action (here, prints "URL CLICKED" on command 
prompt) (We can trigger other actions, e.g. sending an email to a person) 

url_email.py - running this file sends an HTML email to a customer, with URL of web server created in website.py. 

SECTION 1 is functioning as per expectations. 



SECTION 2: There is an invisible tracking pixel in an email. When user opens the email, a notification is printed on the command terminal 

website_pixel.py - running this file creates a gif image in a Flask web server. If the server recieves a GET request, it triggers an action (here, prints 
"ACTION TRIGGERED" on command prompt) 

pixel.py - running this file sends an HTML email to the user with link of the image in our web server

Current errors in Section 2: opening the email is not sending a GET request to our web server 




