from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("googleapp/",include("googleapp.urls")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]