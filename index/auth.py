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

'''2. 授权的校验与验证
from django.contrib.auth.models import User
User.objects.all()
<QuerySet [<User: admin>, <User: bookstore>, <User: bookstore2>]>

# 给用户添加、删除权限的过程其实就是修改 auth_user_user_permissions 表数据记录的过程
from django.contrib.auth.models import User, Permission

user=User.objects.get(username='bookstore')
add_book=Permission.objects.get(codename='add_book')
change_book=Permission.objects.get(codename='change_book')
#查看实例对象所有权限若无任何返回值是空集合set
user.get_all_permissions()

#将user的权限设置为当前权限值，之前权限的会自动去掉
user.user_permissions.set([add_book])
#在当前权限的基础新增权限
user.user_permissions.add(change_book)
#同时也可接受多个权限值
user.user_permissions.add(add_book,change_book)
#删除权限
user.user_permissions.remove(change_book)
#清空所有权限
user.user_permissions.clear()


mysql> select * from auth_user_user_permissions;
+----+---------+---------------+
| id | user_id | permission_id |
+----+---------+---------------+
|  5 |       2 |            29 |
|  6 |       2 |            30 |
+----+---------+---------------+
2 rows in set (0.00 sec)


# 用户组添加 权限
# 介绍 Group 的时候曾经说过，属于某个用户组的用户会自动拥有用该户组被授予的权限。
from django.contrib.auth.models import User, Permission,Group
add_book=Permission.objects.get(codename='add_book')
change_book=Permission.objects.get(codename='change_book')
#创建用户组
    Group.objects.get_or_create(name="library")
group_book=Group.objects.get(name="library")
#添加用户组全权限
group_book.permissions.set([add_book,change_book])
#查当前用户权限
user.get_all_permissions()

# 判断user拥有权限
has_perm('appname.codename(权限编码)')
has_perms(["add_book","change_book"])
'''