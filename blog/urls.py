#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import path
from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.post_list),
]
