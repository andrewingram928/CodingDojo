from django.urls import path, include

urlpatterns = [
    path('', include('first_orm_app.urls')),
]
