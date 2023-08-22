from django.urls import path
from . import views


urlpatterns = [
    path('login_user', views.login_user, name="login2"),
    path('logout_user', views.logout_user, name="logout2"),
    path('register_user', views.register_user, name="register_user"),
]