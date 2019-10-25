import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.qq.com'
mail_user = '471052032'
mail_pass = 'jeytodcrejjvbibi'

subject = 'An Email Alert'
sender = '471052032@qq.com'
receiver = 'zzxy123007@163.com'

msg = MIMEText('The body of the email is here')

# msg['Subject'] = 'An Email Alert'
# msg['From'] = '471052032@qq.com'
# msg['To'] = 'zzxy123007@163.com'
msg['subject'] = Header(subject)
msg['From'] = Header('sino')
msg['To'] = Header('clover')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    # smtpObj.send_message(msg)
    smtpObj.sendmail(sender, receiver, msg.as_string())
    smtpObj.quit()
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print('无法发送邮件')
    print(e)
