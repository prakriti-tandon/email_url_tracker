from flask import Flask, request, abort

app=Flask(__name__)

@app.route('/',methods=['GET','POST']) #link to the created web server is http://127.0.0.1:5000/



def webhook():
    #print(12345)
    if request.method=='GET': #trigger for webhook
        print("URL CLICKED") #action of webhook
        return 'success',200
    else:
        abort(400)

if __name__=='__main__':
    app.run()
