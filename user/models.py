from django.db import models


# Create your models here.
class User(models.Model):  # 创建用户信息表
    username = models.CharField(max_length=24, verbose_name='用户注册')
    password = models.CharField(max_length=50, verbose_name='密码')

    # 定义chocies参数的对应关系，以元组（或者列表）的形式进行表述：
    # choices = (
    #     ('M', '男性'),
    #     ('F', '女性'),
    # )
    # gender = models.CharField(max_length=10, choices=choices, default='M')

    def __str__(self):
        return '(u：%s)' % (self.username)


# User.objects.create(username="hh", password="202cb962ac59075b964b07152d234b70")