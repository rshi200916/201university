import random
import smtplib
from email.mime.text import MIMEText

import logging


from .paramter import *

logger = logging.getLogger('django')


def code(n=6):
    s = ''
    for i in range(n):
        number = random.randint(0,9)
        upper = chr(random.randint(65,90))
        lower = chr(random.randint(97,122))
        char = random.choice([number,upper, lower])
        s += str(char)
    return s


def send_email(send_to, content, Subject='验证码'):

    message = MIMEText(content, type, charset)
    message['From'] = send_by
    message['To']= send_to
    message['Subject'] = Subject
    stmp = smtplib.SMTP_SSL(mail_host, port, charset)
    stmp.login(send_by,password)
    stmp.sendmail(send_by, send_to, message.as_string())


def send_email_code(send_to):
    verification_code = code()

    content = '您的验证码是{}，若非本人操作，请忽略'.format(verification_code)
    try:
        send_email(send_to=send_to,content=content)
        return verification_code

    except Exception as error:
        logger.error(error)
        return False





