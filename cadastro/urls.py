from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/delete/<int:id>/', views.deletar_usuario, name='deletar_usuario'),
]
