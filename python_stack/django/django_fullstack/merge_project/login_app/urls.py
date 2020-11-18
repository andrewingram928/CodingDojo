from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/register', views.register),
    path('login/success', views.success),
    path('login/login', views.login),
    path('login/logout', views.logout),
]