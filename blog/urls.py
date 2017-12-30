#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import re_path
from django.conf.urls import include,url
from . import views

urlpatterns = [
    re_path(r'^$',views.post_list),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
]
