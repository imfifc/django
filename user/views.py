import hashlib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
# 用户的登录逻辑处理
from user.models import User


def login_view(request):
    # 处理GET请求
    if request.method == 'GET':
        # 1, 首先检查session，判断用户是否第一次登录，如果不是，则直接重定向到首页
        print(111, dir(request.session))
        if 'username' in request.session:  # request.session 类字典对象
            return HttpResponseRedirect('/index/allbook')
        # 2, 然后检查cookie，是否保存了用户登录信息
        if 'username' in request.COOKIES:
            # 若存在则赋值回session，并重定向到首页
            request.session['username'] = request.COOKIES['username']
            return HttpResponseRedirect('/index/allbook')
        # 不存在则重定向登录页，让用户登录
        return render(request, 'user/login.html')

    # 处理POST请求
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        m = hashlib.md5()
        m.update(password.encode())
        password_m = m.hexdigest()
        print("用户，加密密码 ", username, password_m)  # hh 123
        # 判断输入是否其中一项为空或者格式不正确
        if not username or not password:
            error = '你输入的用户名或者密码错误 !'
            return render(request, 'user/login.html', locals())
        # 若输入没有问题则进入数据比对阶段，看看已经注册的用户中是否存在该用户
        users = User.objects.filter(username=username, password=password_m)
        # print("users", users,"users[0]",users[0])  # users <QuerySet [<User: 用户：hh>]>

        # 由于使用了filter, 所以返回值user是一个数组，但是也要考虑其为空的状态，即没有查到该用户
        if not users:
            error = '用户不存在或用户密码输入错误!!'
            return render(request, 'user/login.html', locals())
        # 返回值是个数组，并且用户名具备唯一索引，当前用户是该数组中第一个元素
        users = users[0]
        request.session['username'] = username
        print("session", request.session.keys(),
              request.session.values())  # dict_keys(['username']) ,dict_values(['hh'])
        response = HttpResponseRedirect('/index/allbook/')
        # 检查post 提交的所有键中是否存在 isSaved 键
        print("request.POST.keys()", request.POST.keys())
        if 'isSaved' in request.POST.keys():
            # 若存在则说明用户选择了记住用户名功能，执行以下语句设置cookie的过期时间
            response.set_cookie('username', username, 60 * 60 * 24 * 7)
        return response


def logout_view(request):
    # 实现退出功能
    # 删除session
    if 'username' in request.session:
        del request.session['username']
    resp = HttpResponseRedirect('/user/index/')
    # 删除cookie
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    return resp


def index(request):
    # user = request.session.values()
    user = request.COOKIES.get('sessionid')

    return render(request, "user/index.html", locals())


"""
#保存session的值到服务器
request.session['KEY'] = VALUE
#获取session的值
VALUE = request.session['KEY']
VALUE = request.session.get('KEY', 缺省值)
#删除session的值
del request.session['KEY']
request.session.flush()#删除所有session
"""
