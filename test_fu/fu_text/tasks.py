import time
from celery import task
from django.conf import settings
from django.core.mail import send_mail

@task
def test_celery():
    print('start send email')
    msg = '<a href="http://www.itcast.cn/subject/pythonzly/index.shtml" target="_blank">点击激活</a>'
    send_mail('注册激活', '', settings.EMAIL_FROM,
              ['634538608@qq.com'],
              html_message=msg)

    print('end')
