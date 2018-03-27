import os
import time
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendsimplemail(warning):
    msg = MIMEText(warning)
    msg['Subject'] = 'python first mail'
    msg['From'] = 'root@localhost'
    try:
        smtp = smtplib.SMTP()
        smtp.connect(r'smtp.163.com')
        smtp.login('lizhuhe@163.com','mima')
        smtp.sendmail('lizhuhe@163.com','lizhuhe@163.com' ,msg.as_string())
        smtp.close()
    except Exception:
        print('SMTP Error!')

while True:
    http_status = os.popen('netstat -tulnp | grep httpd','r').readlines()
    try:
        if http_status == []:
            new_http_status = os.popen('netstat -tulnp | grep httpd','r').readlines()
            str1 = ''.join(new_http_status)
            is_80 = str1.split()[3].split(':')[-1]
            if is_80 != '80':
                print ('httpd start failed')
            else:
                print ('httpd start succeed')
                sendsimplembail(waring = "This is a warning!!!")
        else:
            print ('httpd status is ok!')

        time.sleep(5)
    except KeyboardInterrupt:
        sys.exit('\n')

