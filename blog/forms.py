#!/usr/bin/env python3
#! -*- coding: UTF-8 -*-
__time__ = '2017/12/30 0030 下午 9:45'
__author__ = 'Zhangge'

from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)