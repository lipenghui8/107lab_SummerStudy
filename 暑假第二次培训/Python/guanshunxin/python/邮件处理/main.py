# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# sender="2984044599@qq.com"
# password="gzeruzudwftzdhbj"
# receiver=["540625710@qq.com",]
# message=MIMEText("收到请回复","plain","utf-8")
# message["From"]=Header("python邮件","utf-8")
# message["To"]=Header("邮件","utf-8")
# message["Subject"]="Python SMTP 发送邮件"
# try:
#     smtp=smtplib.SMTP_SSL("smtp.qq.com",465)
#     smtp.login(sender,password)
#     smtp.sendmail(sender,receiver,message.as_string())
#     print("邮件已发送")
# except smtplib.SMTPException as e:
#     print("Error！发送失败",e)
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# sender="2984044599@qq.com"
# password="gzeruzudwftzdhbj"
# receiver=["2984044599@qq.com",]
# mail_msg="""
# <div style="background-color:yellow; width:100%;height:400px">
# <p style="color:black;font-size:20px;width:100%;height:50%;">你身上的颜色</p>
# <p style="color:black;font-size:20px;width:100%;height:50%;">复制下来给你好康的www.b3u5.com</p>
# </div>
# """
# message=MIMEText(mail_msg,"html","utf-8")
# message["From"]=Header("python邮件","utf-8")
# message["To"]=Header("邮件","utf-8")
# message["Subject"]="Python SMTP 发送邮件"
# try:
#     smtp=smtplib.SMTP_SSL("smtp.qq.com",465)
#     smtp.login(sender,password)
#     smtp.sendmail(sender,receiver,message.as_string())
#     print("邮件已发送")
# except smtplib.SMTPException as e:
#     print("Error！发送失败",e)
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
# sender="2984044599@qq.com"
# password="gzeruzudwftzdhbj"
# receiver=["2984044599@qq.com",]
# message=MIMEMultipart()
# message["From"]=Header("python邮件","utf-8")
# message["To"]=Header("邮件","utf-8")
# message["Subject"]="Python SMTP 发送邮件"
# mail_msg="""
# <div style="background-color:yellow; width:100%;height:400px">
# <p style="color:black;font-size:20px;width:100%;height:50%;">你身上的颜色</p>
# <p style="color:black;font-size:20px;width:100%;height:50%;">复制下来给你好康的www.b3u5.com</p>
# </div>
# """
# message.attach(MIMEText(mail_msg,"html","utf-8"))
# attached_file=MIMEText(open(__file__,encoding="utf-8").read(),"base64","utf-8")
# attached_file["Content-Disposition"]='attachment;filename="main.py"'
# message.attach(attached_file)
#
# try:
#     smtp=smtplib.SMTP_SSL("smtp.qq.com",465)
#     smtp.login(sender,password)
#     smtp.sendmail(sender,receiver,message.as_string())
#     print("邮件已发送")
# except smtplib.SMTPException as e:
#     print("Error！发送失败",e)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
sender="2984044599@qq.com"
password="gzeruzudwftzdhbj"
receiver=["1084118748@qq.com",]
message=MIMEMultipart("related")
message["From"]=Header("python邮件","utf-8")
message["To"]=Header("邮件","utf-8")
message["Subject"]="Python SMTP 发送邮件"
msg_content=MIMEMultipart("alternative")
mail_msg="""

<p style="color:black;font-size:30px;width:100%;height:60px;background-color:yellow;text-align：center;">你身上的颜色</p>
<p style="color:black;font-size:30px;width:100%;height:100px;text-align：center;margin-bottom:100px;">复制下来给你好康的www.b3u5.com</p>
<img src="cid:img1" style="width:100%;height:340px;>

"""
msg_content.attach(MIMEText(mail_msg,"html","utf-8"))
message.attach(msg_content)
with open("1.jpg","rb")as f:
    img1=MIMEImage(f.read())
img1.add_header("Content-ID","img1")
message.attach(img1)
try:
    smtp=smtplib.SMTP_SSL("smtp.qq.com",465)
    smtp.login(sender,password)
    smtp.sendmail(sender,receiver,message.as_string())
    print("邮件已发送")
except smtplib.SMTPException as e:
    print("Error！发送失败",e)