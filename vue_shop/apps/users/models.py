from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """
    用户模型
    """
    # 这里设置null原因是我们注册时是用的手机注册，不会包括用户名
    username = models.CharField(max_length=30,unique=True,null=True,blank=True,verbose_name="姓名")
    # 设置出生日期用以推算年龄
    birthday = models.CharField(max_length=100,null=True,blank=True,verbose_name="出生年月")
    #
    mobile = models.CharField(max_length=11,verbose_name='电话')
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female",u"女")),default="female",verbose_name="性别")
    email = models.EmailField(max_length=100,null=True,blank=True,verbose_name='邮箱')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class VerifyCode(models.Model):
    """
    短信验证码保存至数据库中，回填验证码进行验证，也可以保存在redis中
    """
    code = models.CharField(max_length=10,verbose_name="验证码")
    mobile = models.CharField(max_length=11,verbose_name="手机号码")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

