from django.urls import path, include

urlpatterns = [
    # Основные
    path('', include('project.routers')),
]