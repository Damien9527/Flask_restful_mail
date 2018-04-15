#!/usr/bin/env python
# coding:utf-8
from flask import Flask,request
import threading
from flask_mail import Mail, Message
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.139.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'xw9527@139.com'
app.config['MAIL_PASSWORD'] = '******'
app.config['MAIL_DEFAULT_SENDER'] = 'xw9527@139.com'
mail = Mail(app)

@app.route('/sendMail',methods=['POST','GET'])
def index():
    messages = request.values.to_dict()
    title = messages['title']
    content = messages['content']
    tolist = messages['tolist']
    tolist = str(tolist).split(',')
    cc = messages['cc']
    status = sendmail(title,content,tolist,cc)
    return status

def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def sendmail(title,content,tolist,cc):
    msg = Message(title , recipients=tolist,cc=cc)
    msg.html = content
    thr = threading.Thread(target=send_async_email, args=[app,msg])#创建线程
    thr.start()
    return thr


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
