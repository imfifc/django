'''
pip3 install uwsgi

使用上述命令安装 uWSGI，安装完成后在 BookStore 项目的根目录下，新建 uwsgi.ini 配置文件（和 manage.py 文件同级目录），并在该文件中进行如下配置：
[uwsgi]
# 套接字方式的 IP地址:端口号
# socket=127.0.0.1:8000
# Http通信方式的 IP地址:端口号
http=127.0.0.1:8000
#上述两种方式选择其一，在使用Nginx需要使用socket
# 项目当前工作目录自行配置
chdir=/home/.../.../my_projectname 这里需要换为项目文件夹的绝对路径
# 项目中wsgi.py文件的目录，相对于当前工作目录
wsgi-file=my_project/wsgi.py
#是否启动主进程来管理其他进程
master=true
# 进程个数，根据电脑配置设置
process=4
# 每个进程的线程个数
threads=2
# 服务的pid记录文件
pidfile=uwsgi.pid
# 服务的日志文件位置
daemonize=uwsgi.log



然后修改 settings.py 文件将其设置为适合线上生产环境使用，如下所示：
DEBUG=False                    #关闭调试模式
ALLOWED_HOSTS = ['*']   #任何ip都可以访问


启动与测试uWSGI服务器
配置完成后，我们就可以使用下面的命令启动 uWSGI 了：
启动 uwsgi 命令
$ cd 项目文件夹
$ sudo uwsgi --ini uwsgi.ini
停止 uwsgi 命令
$ cd 项目文件夹
$ sudo uwsgi --stop uwsgi.pid
'''