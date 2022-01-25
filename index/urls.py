from django.urls import path, re_path
from index import views
from index.views import LoginView1

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
    path('all_book/', views.BookName),
    path('allauthor/', views.authorname),
    path('annotate/', views.test_annotate),
    path('logincbv/', LoginView1.as_view(), name='home'),
    # 使用as_view()方法创建类实例
    # http://127.0.0.1:8000/admin/index/book/
    path('login1/', views.login1),  # ? 为啥2级路由下 响应不行 http://127.0.0.1:8000/index/login/   --- http://127.0.0.1:8000/login/

    path('set_cookie/', views.set_cookie_view),
    path('get_cookie/', views.get_cookie_view),

    path('search_ttile_form/', views.search_ttile_form),
    path('search_title/', views.search_title),

    path('search_ttile_form2/', views.search_ttile_form2),
    path('search_title2/', views.search_title2),
    path('book_not_list/', views.book_not_list),

    path('book_table/', views.book_table),
    path('add_book/', views.add_book),
    path('update_book/<int:book_id>/', views.update_book),
    path('delete_book/<int:book_id>/', views.delete_book),
    # path('delete_book/', views.delete_book),
    path('user_add_form/', views.user_add_form),
    path('page_test/', views.page_test),
    # path('login_views/', views.login_views),
]
