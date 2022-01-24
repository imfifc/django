from django.contrib.auth.models import User


class EmailBackend(object):
    def authenticate(self, request, **credentials):
        # 获取邮箱的认证信息即邮箱账号实例
        email = credentials.get('email', credentials.get('username'))
        try:
            user = User.objects.get(email=email)
        except Exception as error:
            print(error)
        else:
            # 检查用户密码
            if user.check_password(credentials["password"]):
                return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)  # 提供了一个 pk 字段来代表主键 ID
        except Exception as e:
            print(e)
            return None


'''
In [1]: from django.contrib.auth import authenticate
In [2]: user=authenticate(username="bookstore",password="python_django")
In [3]: user.backend
Out[3]: 'django.contrib.auth.backends.ModelBackend' #返回Django默认后端
In [4]: user.backend
Out[4]: 'django.contrib.auth.backends.ModelBackend'
In [5]: user=authenticate(username="bookstore",password="python")
In [6]: user is None
Out[6]: True
In [7]: user=authenticate(email="123@163.com",password="python_django")
In [8]: user.bachend
Out[8]: 'user.backends.EmailBackend' #返回自定义后端
'''