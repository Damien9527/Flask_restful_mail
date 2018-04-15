#!/usr/bin/env python
# coding:utf-8
from flask import Flask,request
from flask_mail import Mail, Message
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.139.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'xw9527@139.com'
app.config['MAIL_PASSWORD'] = 'xw1916139'
app.config['MAIL_DEFAULT_SENDER'] = 'xw9527@139.com'
mail = Mail(app)

import threading
from flask_request_params import bind_request_params

app.before_request(bind_request_params)

@app.route('/sendMail',methods=['POST','GET'])
def index():
    messages = request.values.to_dict()
    title = messages['title']
    content = messages['content']
    tolist = messages['tolist']
    #tolist = request.args.get('tolist')
    tolist = str(tolist).split(',')
    status = sendmail(title,content,tolist)
    return "200"

def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def sendmail(title,content,tolist):
    msg = Message(title , recipients=tolist,bcc=['xiewei@staff.sina.com.cn'])
    msg.html = content
    thr = threading.Thread(target=send_async_email, args=[app,msg])#创建线程
    thr.start()
    return thr
    mail.send(msg)
    return 'success'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)