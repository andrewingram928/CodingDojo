from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_course', views.create),
    path('courses/destroy/<int:course_id>', views.destroy),
    path('courses/comments/<int:course_id>', views.comment),
]