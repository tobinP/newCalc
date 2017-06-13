from django.conf.urls import url

from . import views

app_name = 'calc'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^$', views.result, name='result'),
    # url(r'^(?P<question>[0-9]+)/$', views.result, name='result'),
    url(r'^(?P<test>[0-9]+)/result/$', views.result, name='result'),
    # url(r'^$', views.result, name='result'),
]
