from django.urls import path, include

urlpatterns = [
    path('', include('random_generator_app.urls'))
]
