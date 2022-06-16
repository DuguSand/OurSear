"""定义searcher的URL模式"""
from django.urls import re_path

from . import views

urlpatterns=[
    #搜索主页
    re_path(r'^$', views.index, name='index'),
    #特定主题
    re_path(r'^(?P<topic_id>\d+)/$', views.topic, name='topic'),
]