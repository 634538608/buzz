from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from fu_text import tasks
import time

# Create your views here.
def index(request):
    context = {'haha':'第三方包'}
    return render(request,'fu_text/index.html',context)

def detail(request):
    text = request.POST['gcontent']
    context = {'text': text}
    return render(request, 'fu_text/detail.html', context)


def send_email(request):
    msg = '<a href="http://www.itcast.cn/subject/pythonzly/index.shtml" target="_blank">点击激活</a>'
    send_mail('注册激活', '', settings.EMAIL_FROM,
              ['634538608@qq.com'],
              html_message=msg)
    # tasks.send_email.delay()
    return HttpResponse('ok')

def test_celery(request):
    # print('hello')
    # time.sleep(2)
    # print('world')
    tasks.test_celery.delay()

    return HttpResponse('hello world')

