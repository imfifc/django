"""BookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test_html),
    path('test2/', views.test2_html),
    path('test3/', views.test3_html),
    path('test_if/', views.test_if),
    path('test_if2/', views.test_if2),
    path('test_for/', views.test_for),
    path('test_for2/', views.test_for2),
    path('test_filter/', views.test_filter, name='hello1'),
    path('test_url/', views.test_url),

    path('Hello_MyWeb/<int:id>', views.Hello_MyWeb, name='hello'),
    path('test_lable/', views.user_define_lable),
    path('test_inclusion_lable/', views.inclusion_lable),
    path('test_assignment_tag/', views.assignment_tag),
    path('equal_lable/', views.equal_lable),
    path('ifchanged_lable/', views.ifchanged_lable),
    path('cycle_lable/', views.cycle_lable),
    path('user_define_filter/', views.user_define_filter),

    # path('index/', include('index.urls', namespace='first')),
    path('index/', include('index.urls')),
    path('user/', include('user.urls')),

    # path('login/', views.login),

]
