# -*- coding: UTF-8 -*-

import smtplib
import sys
from email.header import Header
from email.mime.text import MIMEText

# 公有参数列表
commonParameter1_flowId = sys.argv[1]
commonParameter2_repoName = sys.argv[2]
commonParameter3_platform = sys.argv[3]

# 私有参数列表
emailAddress = sys.argv[4]
previewUrl = 'UNKNOWN'
showButton = ''
if len(sys.argv) >= 6:
    previewUrl = sys.argv[5]
    showButton = '点击预览项目'

# 以下邮件代发服务器账号仅供测试
# 此处请填写成自己的邮件代发服务器配置（基于SMTP协议）
mail_host = 'smtp.qq.com'
server_port = 465
mail_user = 'easyci@qq.com'
mail_pass = 'mnjubtchvdmujcgg'

sender = mail_user
receivers = [emailAddress]

emailMsg = "<center><h2>「" + commonParameter2_repoName + "」仓库项目构建结束</h2></center><center><p><a href=\"" + previewUrl + "\" style=\"color:red\">" + showButton + "</a></p></center>"
message = MIMEText(emailMsg, 'html', 'utf-8')
message['From'] = Header('EasyCI <' + mail_user + '>', 'utf-8')
message['To'] = Header('<' + emailAddress + '>', 'utf-8')
subject = '项目「' + commonParameter2_repoName + '」任务构建通知'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL()
    smtpObj.connect(mail_host, server_port)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('Send Success\n0')
except smtplib.SMTPException:
    print('Error: Send Failed\n401')
