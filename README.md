# Flask_restful_mail


#支持异步发送邮件
#使用方法参考：


curl http://ip:5000/sendMail -d "title=$title&content=$message" -d "tolist=mail@qq.com" -d "cc=mailcc@qq.com"

title 为标题
content 为邮件内容
tolist 为主送人
cc 为抄送人
