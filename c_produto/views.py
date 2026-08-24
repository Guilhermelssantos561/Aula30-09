from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def c_produto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        estoque = request.POST.get("estoque")
        preco = request.POST.get("preco")
        foto_url = request.POST.get("foto_url")

        if preco:
            preco = preco.replace(",", ".")  # aceita vírgula

        Produto.objects.create(
            nome=nome,
            estoque=estoque,
            preco=preco,
            foto_url=foto_url
        )
        return redirect("c_produto")

    produtos = Produto.objects.all()
    return render(request, "c_produto.html", {"produtos": produtos})


def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        produto.nome = request.POST.get("nome")
        produto.estoque = request.POST.get("estoque")
        preco = request.POST.get("preco")
        if preco:
            preco = preco.replace(",", ".")
        produto.preco = preco
        produto.foto_url = request.POST.get("foto_url")
        produto.save()
        return redirect("c_produto")
    return render(request, "editar_produto.html", {"produto": produto})


def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect("c_produto")
