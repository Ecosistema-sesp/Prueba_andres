from django.urls import path
from . import views

urlpatterns = [
    # Define las rutas específicas para la aplicación 'pr'
    path('someview/', views.some_view, name='some_view'),
    # otras rutas aquí
]
