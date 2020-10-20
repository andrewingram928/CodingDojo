from django.urls import path
from . import views
urlpatterns = [
	path('', views.landing),
    path('process_money', views.process),
    path('define_rules', views.rules),
    path('game_complete', views.complete),
]