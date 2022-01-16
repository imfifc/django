from django.urls import path
from index import views

app_name = 'index'  # 注册 写在开始位置即可

urlpatterns = [
    # 127.0.0.1:8000/index/test 访问子模板
    path('test/', views.index_html, name='detail_hello'),
    # 127.0.0.1:8000/index/base 访问父模板
    path('base/', views.base_html),
    path('redict/', views.redict_url),
    path('reverse/', views.test_to_reverse),
]
