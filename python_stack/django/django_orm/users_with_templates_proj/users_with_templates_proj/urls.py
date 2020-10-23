from django.urls import path, include

urlpatterns = [
    path('', include('users_template_app.urls')),
]
