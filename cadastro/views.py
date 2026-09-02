
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator

def cadastro(request):
    return render(request, "cadastro.html")

def deletar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('lista_usuarios')

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "lista_usuarios.html", {"usuarios": usuarios})

def ativar_conta(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Sua conta foi ativada com sucesso! Você já pode fazer login.')
    else:
        messages.error(request, 'O link de ativação é inválido ou expirou.')

    return redirect('login')

