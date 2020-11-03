from django.urls import path, include

urlpatterns = [
    path('', include('course_app.urls')),
]
