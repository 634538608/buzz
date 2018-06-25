from fu_text import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.index ,name='index'),
    url(r'^detail$', views.detail, name='index'),
    url(r'^send_email$', views.send_email, name='send_email'),
    url(r'^test_celery$', views.test_celery, name='test_celery'),
]