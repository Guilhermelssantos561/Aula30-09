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
from django.urls import path
from django.contrib.auth import views as auth_views

from cadastro import views as cadastro_views
from login.views import login_view
from login.views import painel_redirect
from carrinho import views as carrinho_views
from c_produto import views as c_produto_views
from . import views
from painel.views import painel_principal

urlpatterns = [
    path('c_produto/', c_produto_views.c_produto, name='c_produto'),
    path('editar/<int:id>/', c_produto_views.editar_produto, name='editar_produto'),
    path('excluir/<int:id>/', c_produto_views.excluir_produto, name='excluir_produto'),

    path('admin/', admin.site.urls),

    path('cadastro/', cadastro_views.cadastro, name='cadastro'),
    path('ativar-conta/<uidb64>/<token>/',cadastro_views.ativar_conta,name='ativar_conta'),

    path('login/', login_view, name='login'),

    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),

    path('carrinho/', carrinho_views.carrinho, name='carrinho'),
    path('carrinho/remover/<int:item_id>/',carrinho_views.remover_item,name='remover_item'),

    path('app/', views.app, name='app'),
    path('painel/', painel_principal, name='painel'),
    path('painel/', painel_redirect, name='painel_redirect'),
      # Rota principal após o login
    path('painel/', login_view.painel_redirect, name='painel_redirect'),
    
    # Rotas específicas de cada nível
    path('painel/administrador/', painel_views.view_administrador, name='view_administrador'),
    path('painel/diretoria/', painel_views.view_diretoria, name='view_diretoria'),
    path('painel/gerencia-geral/', painel_views.view_gerencia_geral, name='view_gerencia_geral'),
    path('painel/gerencia/', painel_views.view_gerencia, name='view_gerencia'),
    path('painel/supervisao/', painel_views.view_supervisao, name='view_supervisao'),
    path('painel/atendente/', painel_views.view_atendente, name='view_atendente'),
    path('painel/caixa/', painel_views.view_caixa, name='view_caixa'),
]