from django.urls import path, re_path
from index import views

"""
str，匹配除了路径分隔符（/）之外的非空字符串，这是默认的形式；
int，匹配正整数，包含0；
slug，匹配字母、数字以及横杠、下划线组成的字符串；
uuid，匹配格式化的 uuid，如 075194d3-6885-417e-a8a8-6c931e272f00；
path，匹配任何非空字符串，包含了路径分隔符。

第一是可以将捕获到的字符值转换为对应的类型；
第二是对 URL 中传值的一种限制，避免视图处理出错
(?P<name>pattern) 
"""
app_name = 'index'  # 注册 写在开始位置即可

urlpatterns = [
    # 127.0.0.1:8000/index/test 访问子模板
    path('test/', views.index_html, name='detail_hello'),
    # 127.0.0.1:8000/index/base 访问父模板
    path('base/', views.base_html),
    path('redict/', views.redict_url),
    path('reverse/', views.test_to_reverse),
    # re_path('test/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[^/]+)/', views.article_test),
    # re_path(r'^test/(?P<year>[0-9]{4})/$', views.year_test),
    # path('test/<int:year>/', views.year_test),
    path('allbook/', views.BookName),
    path('allauthor/', views.authorname),
    path('annotate/', views.test_annotate),

]
