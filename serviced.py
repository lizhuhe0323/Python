import os
import time
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendsimplemail(warning):
    sender = 'luke.li@luckypai.com'
    receivers = ['luke.li@luckypai.com']
    subject = 'Python SMTP测试'
    msg = MIMEText('Python 邮件发送测试','plain','utf-8')
    msg['Subjectubject'] = Header(subject,'utf-8')
    msg['From'] = Header('Python Check','utf-8')
    msg['To'] = Header('测试','utf-8')
    try:
        smtp = smtplib.SMTP('mail.51lepai.com')
        #smtp = smtplib.SMTP_SSL(mail.51lepai.com, 465)
        #smtp.login('mail_user', 'mail_pass')
        smtp.sendmail(sender,receivers,msg.as_string())
        print('邮件发送成功!')
    except Exception:
        print('邮件发送失败!')

while True:
    http_status = os.popen('netstat -tulnp | grep httpd','r').readlines()
    try:
        if http_status == []:
            new_http_status = os.popen('netstat -tulnp | grep vino-server','r').readlines()
            str1 = ''.join(new_http_status)
            is_80 = str1.split()[3].split(':')[-1]
            if is_80 != '80':
                print ('httpd服务启动失败')
                sendsimplemail(warning="This is a warning!!!")
            else:
                print ('httpd服务启动成功')
        else:
            print ('httpd状态正常!')

        time.sleep(5)
    except KeyboardInterrupt:
        sys.exit('\n')

