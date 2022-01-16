from django.urls import path
from index import views

urlpatterns = [
    # 127.0.0.1:8000/index/test 访问子模板
    path('test/', views.index_html),
    # 127.0.0.1:8000/index/base 访问父模板
    path('base/', views.base_html)]
