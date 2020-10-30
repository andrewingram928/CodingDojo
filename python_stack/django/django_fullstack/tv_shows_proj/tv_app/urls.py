from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/<int:show_id>', views.one_show),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/edit!', views.edit_show_process),
    path('shows/<int:show_id>/destroy', views.destroy),
    path('shows/create', views.create_show),
    path('shows/create!', views.create_show_process),
]