from flask import Flask, request, abort, send_file
import base64
import logging
import io

#logger.setLevel(logging.INFO)


app=Flask(__name__)

@app.route('/pixel.gif',methods=['GET','POST'])  #link to the image is http://127.0.0.1:5000/pixel.gif


def returnPixel():
    gif = 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='
    gif_str = base64.b64decode(gif) #tracking image
    logging.warning("Action Tracked") #prints Action Tracked on the command prompt 
    return send_file(io.BytesIO(gif_str), mimetype='image/gif')


if __name__=='__main__':
    app.run()
