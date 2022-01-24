from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, get_user_model
import django.db.models.options

# User模型创建用户与超级用户 create_superuser
user = User.objects.create_user('bookstore', '123@163.com', 'python_django')
user.set_password('123')
user.save()
# 用户可以属于任意数量的组。组中的用户自动拥有授予该组的所有权限;  组还可以方便地对用户进行分类，以便对他们应用一些标签或扩展功能

group = Group.objects.create(name="reader")
user = User.objects.get(username="bookstore")  # auth_user
user.groups.add(group)
user.groups.all()
# < QuerySet[ < Group: reader >] >

# 认证功能
user = authenticate(username="bookstore", password="python_django")
user  # <User: bookstore>

user = authenticate(username="bookstore", password="python")
# user is None
# True

get_user_model()
# <class 'django.contrib.auth.models.User'>
'''
# 使用自定义User model时
>>> from django.contrib.auth import get_user_model
>>> get_user_model()
<class 'xxx.models.NewUser'>
# get_user_model()实际获取的是settings.AUTH_USER_MODEL指定的User model
'''

'''
# self.default_permissions = ('add', 'change', 'delete', 'view')
Django 为 User 模型自动创建的 4 个可选权限名分别为:
查看用户(view)：user.view_article
创建用户(add)：user.add_article
更改用户(change)：user.change_article
删除用户(delete)：user.delete_article

user_username.has_perm('user.add_article')
user_username.has_perm('user.change_article')


user_username.get_group_permissions()
user_username.get_all_permissions()
'''