from django.urls import path
from . import views
urlpatterns = [
	path('', views.landing),
	path('generate_again', views.generate_again),
	path('generated', views.generated),
	path('first_generate', views.first_generate),
	path('reset', views.reset),
]