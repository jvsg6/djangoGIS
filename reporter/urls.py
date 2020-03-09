from django.urls import path, include

from . import views

urlpatterns = [
    path('details/<int:pk>/', views.accidentDetails, name='accidentDetails'),
    ]