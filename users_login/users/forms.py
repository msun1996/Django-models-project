# -*- coding:utf8 -*-
from django import forms

from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class RegisterEmailForm(forms.Form):
    username = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})