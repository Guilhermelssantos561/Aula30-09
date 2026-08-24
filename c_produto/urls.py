from django.urls import path
from . import views

urlpatterns = [
    path('', views.c_produto, name='c_produto'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
]
