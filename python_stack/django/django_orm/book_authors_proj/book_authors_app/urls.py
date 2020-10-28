from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('book/<int:book_id>', views.view_book),
    path('add_author_from_instance', views.add_author_from_instance),
    path('add_book_from_instance', views.add_book_from_instance),
    path('view_authors', views.view_authors),
    path('author/<int:author_id>', views.view_author),
]