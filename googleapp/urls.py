from django.urls import path

from . import views


urlpatterns = [


    path("signup",views.login,name="signup"),
    path("login/", views.signup, name="login"),
    path("userlogin",views.user_login,name="user_login"),



]
