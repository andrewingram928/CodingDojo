from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/<int:show_id>', views.one_show),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/destroy', views.destroy),
    path('shows/create', views.create_show),
    path('networks/create', views.create_network),
    path('networks/<int:network_id>', views.one_network),
    path('networks/<int:network_id>/edit', views.edit_network),
]