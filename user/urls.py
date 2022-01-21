from django.urls import path
from user import views

urlpatterns = [
    # path('reg/', views.reg_view),
    path('index/', views.index),
    path('login/', views.login_view),
    path('logout/', views.logout_view, name="logout_1"),
    path('reg/', views.reg_view)
]
