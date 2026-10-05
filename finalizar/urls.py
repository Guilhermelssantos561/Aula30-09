# carrinho/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('finalizar/', views.finalizar, name='finalizar'),
]