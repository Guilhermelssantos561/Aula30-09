from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User   # <-- modelo certo
from c_produto.models import Produto

@login_required(login_url='login')
def painel_principal(request):
    produtos = Produto.objects.all()
    usuarios = User.objects.all()   # pega os usuários do auth_user
    return render(request, 'painel/home.html', {
        'produtos': produtos,
        'usuarios': usuarios
    })

