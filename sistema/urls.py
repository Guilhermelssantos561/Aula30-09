"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from cadastro import views as cadastro_views
from login import views as login_views
from carrinho import views as carrinho_views
from c_produto import views as c_produto_views
from . import views   # importa views.py da app sistema

urlpatterns = [
    path('', c_produto_views.c_produto, name='c_produto'),
    path('editar/<int:id>/', c_produto_views.editar_produto, name='editar_produto'),
    path('excluir/<int:id>/', c_produto_views.excluir_produto, name='excluir_produto'),

    path('admin/', admin.site.urls),
    path('cadastro/', cadastro_views.cadastro, name='cadastro'),
    path('login/', login_views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('carrinho/', carrinho_views.carrinho, name='carrinho'),
    path('carrinho/remover/<int:item_id>/', carrinho_views.remover_item, name='remover_item'),

    path('app/', views.app, name='app'),
]








