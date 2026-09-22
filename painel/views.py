from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from login.utils import verificar_grupo

from django.contrib.auth.models import User as Usuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404



@login_required(login_url='login')
def painel_principal(request):
    usuarios = {
         'usuarios': Usuario.objects.all()
    }
    return render(request, 'painel/home.html', usuarios)



@login_required
def view_administrador(request):
    if not verificar_grupo(request.user, 'administradores'):
        raise PermissionDenied # Retorna erro 403 nativo do Django
    return render(request, 'painel/administrador.html')

@login_required
def view_diretoria(request):
    if not verificar_grupo(request.user, 'diretoria'):
        raise PermissionDenied  
    return render(request, 'painel/diretoria.html')

@login_required
def view_gerencia_geral(request):
    if not verificar_grupo(request.user, 'gerencia_geral'):
        raise PermissionDenied
    return render(request, 'painel/gerencia_geral.html')

@login_required
def view_gerencia(request):
    if not verificar_grupo(request.user, 'gerencia'):
        raise PermissionDenied
    return render(request, 'painel/gerencia.html')



@login_required
def view_supervisao(request):

    if not verificar_grupo(request.user, 'supervisao'):
        raise PermissionDenied

    usuarios = User.objects.all()

    busca = request.GET.get('buscar')

    if busca:
        usuarios = usuarios.filter(
            Q(username__icontains=busca) |
            Q(first_name__icontains=busca) |
            Q(last_name__icontains=busca) |
            Q(email__icontains=busca)
        )

    contexto = {
        'usuarios': usuarios,
        'total_usuarios': User.objects.count(),
        'total_ativos': User.objects.filter(is_active=True).count(),
        'total_inativos': User.objects.filter(is_active=False).count(),
        'total_admins': User.objects.filter(is_superuser=True).count(),
    }

    return render(request, 'painel/supervisao.html', contexto)

@login_required
def view_atendente(request):
    if not verificar_grupo(request.user, 'atendente'):
        raise PermissionDenied
    return render(request, 'painel/atendente.html')

@login_required
def view_caixa(request):
    if not verificar_grupo(request.user, 'caixa'):
        raise PermissionDenied
    return render(request, 'painel/caixa.html')


@login_required
def alterar_status(request, user_id):

    usuario = get_object_or_404(User, id=user_id)

    usuario.is_active = not usuario.is_active

    usuario.save()

    return redirect('view_supervisao')