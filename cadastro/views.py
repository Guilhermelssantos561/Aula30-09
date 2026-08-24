
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def cadastro(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem.")
            return redirect("cadastro")

        # Cria usuário
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        user.save()
        messages.success(request, "Conta criada com sucesso!")
        return redirect("login")

    return render(request, "cadastro.html")

