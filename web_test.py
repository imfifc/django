from wsgiref.simple_server import make_server


# 自定义服务器
# 定义服务器调用对象application
def application(environ, start_response):
    """
    :param environ:  #包含所有客户端的请求信息即上下文请求，application从这个参数中获取客户端请求意图
    :param start_response: 一个可调用对象，用于发送http请求状态
    :return: [b'Hello World!\n'] #返回可迭代对象 且必须是字节流，Http是面向字节流协议
     """
    status = '200 OK'
    response_headers = [('Conteny-type', 'text/plain')]  # 响应头是一个列表
    start_response(status, response_headers)  # 返回给server之前调用 start_response
    return [b"Hello World!\n"]  # 返回字节码


# 创建WSGI服务器，指定调用application,这里的调用对象也可以是一个类或者实例
httpeserver = make_server('127.0.0.1', 8000, application)
# 处理请求后退出
httpeserver.handle_request()

'''
WSGI协议：
WSGI（Web Server Gateway Interface）即 Web 服务器网关接口，它是属于一种规范协议，它定义了 Python Web 应用程序与 Web 服务器通信的接口。
需要一种规范或者协议来定义 Web 应用如何与 Web 服务器之间实现交互以及请求的接受与响应的返回
WSGI 协议的出现恰恰解决了上述问题，它可以让 Web 服务器知道如何去调用 Python 应用程序；让 Python 应用程序知道客户端在请求什么，
以及如何返回结果给 Web 服务器，WSGI 实现了 Web 服务器与应用程序之间的交互。

Django 框架同时实现了 WSGI 的 server 和 application。其中内置的 WSGI 服务器是基于 Python 的内置模块 wsgiref 实现的，主要是添加了一些异常处理和错误记录，
但是没有考虑到运行效率，故不适合在生产环境中使用，它主要被使用在开发和测试过程中
'''

'''
PS C:\Users\Administrator\Desktop\book\BookStore> curl   127.0.0.1:8000


StatusCode        : 200
StatusDescription : OK
Content           : {72, 101, 108, 108...}
RawContent        : HTTP/1.0 200 OK
                    Conteny-type: text/plain
                    Content-Length: 13
                    Date: Fri, 28 Jan 2022 16:25:18 GMT
                    Server: WSGIServer/0.2 CPython/3.9.8

                    Hello World!

Headers           : {[Conteny-type, text/plain], [Content-Length, 13], [Date, Fri, 28 Jan 2022 16:25:18 GMT], [Server, WSGIServer/0.2 CPython/3.9.8]}
RawContentLength  : 13

'''


'''
1) uWSGI服务器简单介绍
uWSGI 是当下最流行的一种 WSGI 服务器，同样遵守 WSGI 协议。它可以与各种 Python Web 框架实现兼容，而且配置过程与使用方式都非常简单。我们之前使用 runserver 命令启动项目，通常只是在开发和测试环境中使用。
当开发结束后，完善的项目代码需要在一个高效稳定的环境中运行，这时候可以使用 uWSGI，它是 WSGI 服务器的一种，它可以让 Django、Flask 等开发的 Web 应用站点运行其中。
'''