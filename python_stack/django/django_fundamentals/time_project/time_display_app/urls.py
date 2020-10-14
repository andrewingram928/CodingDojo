from django.urls import path
from . import views
urlpatterns = [
    path('', views.time),
    path('time_display', views.time)
]