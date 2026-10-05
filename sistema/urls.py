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
from cadastro import views as cadastro_view
from login import views as login_view
from app import views as app_view
from painel import views as painel_views
from carrinho import views as carrinho_view
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', app_view.home, name='home'),
    path('cadastro/', cadastro_view.cadastro, name='cadastro'),
    path('ativar/<uidb64>/<token>/', cadastro_view.ativar_conta, name='ativar_conta'),
    path('login/', login_view.login_view, name='login'),
    path('login/mfa/', login_view.mfa_view, name='mfa'),
    path('logout/', login_view.logout_view, name='logout'),
    path('carrinho/', carrinho_view.carrinho, name='carrinho'),
    path('c_produto/', include('c_produto.urls')),
    path('checkout/', carrinho_view.checkout_dados, name='checkout_dados'),
    path('finalizar/',carrinho_view.finalizar,name='finalizar'),
    path(
    'pagar-agora/',carrinho_view.pagar_agora,name='pagar_agora'),



    # Rota principal após o login
    path('painel/', login_view.painel_redirect, name='painel_redirect'),
    
    # Rotas específicas de cada nível
    path('painel/administrador/', painel_views.view_administrador, name='view_administrador'),
    path('painel/diretoria/', painel_views.view_diretoria, name='view_diretoria'),
    path('painel/gerencia-geral/', painel_views.view_gerencia_geral, name='view_gerencia_geral'),
    path('painel/gerencia/', painel_views.view_gerencia, name='view_gerencia'),
    path('painel/supervisao/', painel_views.view_supervisao, name='view_supervisao'),
    path('supervisao/', painel_views.view_supervisao, name='view_supervisao'),
    path('painel/atendente/', painel_views.view_atendente, name='view_atendente'),
    path('painel/caixa/', painel_views.view_caixa, name='view_caixa'),
    path('painel/alterar-status/<int:usuario_id>/', painel_views.alterar_status, name='alterar_status'),
    path('painel/alterar-funcao/<int:usuario_id>/', painel_views.alterar_funcao, name='alterar_funcao'),
    path('painel/excluir-usuario/<int:usuario_id>/', painel_views.excluir_usuario, name='excluir_usuario'),
    path('painel/alterar-permissao/<int:usuario_id>/', painel_views.alterar_permissao, name='alterar_permissao'),
    path('buscar-cliente/', carrinho_view.buscar_cliente, name='buscar_cliente'),
]
