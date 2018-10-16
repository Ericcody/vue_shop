from random import choice

from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render
# 第三方模块并不知道自己的user model 从哪里导入
from django.contrib.auth import get_user_model
# 这个方法会去setting中找AUTH_USER_MODEL
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler,jwt_encode_handler

from vue_shop.settings import APIKEY
from rest_framework.response import Response
from rest_framework import mixins,permissions,authentication
from rest_framework import mixins,status
from users.models import VerifyCode
from utils.yunpian import YunPian
from users.

User = get_user_model()
# 发送验证码是创建model中一条记录的操作
from rest_framework.mixins import CreateModelMixin

# Create your views here.


class CustomBackend(modelBackend):