from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
import json
from django.http import JsonResponse

from .models import Pedido, ItemPedido
from django.contrib.auth.decorators import login_required

def buscar_cliente(request):
    email = request.GET.get('email')

    usuario = User.objects.filter(email=email).first()

    if usuario:
        return JsonResponse({
            'sucesso': True,
            'nome': usuario.first_name,
            'email': usuario.email,
        })

    return JsonResponse({
        'sucesso': False
    })


def remover_item(request, item_id):
    carrinho = request.session.get('carrinho', {})

    if str(item_id) in carrinho:
        del carrinho[str(item_id)]
        request.session['carrinho'] = carrinho

    return redirect('carrinho')


def carrinho(request):
    return render(request, 'carrinho.html')

def checkout_dados(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        usuario = User.objects.filter(email=email).first()

        if usuario is None:

            username = email.split('@')[0]

            contador = 1
            username_original = username

            while User.objects.filter(username=username).exists():
                username = f'{username_original}{contador}'
                contador += 1

            usuario = User.objects.create_user(
                username=username,
                email=email,
                password='123456'
            )

            usuario.first_name = nome
            usuario.save()

        login(request, usuario)

        carrinho_sessao = request.session.get('carrinho', {})

        pedido = Pedido.objects.create(
            usuario=usuario
        )

        for produto_id, item in carrinho_sessao.items():

            ItemPedido.objects.create(
                pedido=pedido,
                produto_id=produto_id,
                nome=item['nome'],
                preco=item['preco'],
                quantidade=item['quantidade']
            )

        request.session['carrinho'] = {}

        return redirect('carrinho')

    return render(request, 'checkout_dados.html')


@login_required
def finalizar(request):
    return render(request, 'finalizar.html')

@login_required
def pagar_agora(request):

    if request.method == 'POST':

        dados = json.loads(request.body)

        itens = dados.get('itens', [])

        pedido = Pedido.objects.create(
            usuario=request.user
        )

        for item in itens:

            ItemPedido.objects.create(
                pedido=pedido,
                produto_id=item.get('id', 0),
                nome=item['nome'],
                preco=item['preco'],
                quantidade=1
            )

        return JsonResponse({
            'sucesso': True
        })

    return JsonResponse({
        'sucesso': False
    })