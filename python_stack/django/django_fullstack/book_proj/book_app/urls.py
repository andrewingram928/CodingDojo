from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('log_out', views.logout),
    path('register', views.register),
    path('books', views.books),
    path('books/add', views.add_book),
    path('books/<int:book_id>', views.one_book),
    path('books/<int:book_id>/delete', views.delete_book),
    path('books/<int:book_id>/favorite', views.favorite_book),
    path('books/my_favorites', views.my_favorites),
]