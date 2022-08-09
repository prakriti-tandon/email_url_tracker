from flask import Flask, request, abort

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])



def webhook():
    #print(12345)
    if request.method=='GET':
        print("URL CLICKED")
        return 'success',200
    else:
        abort(400)

if __name__=='__main__':
    app.run()
