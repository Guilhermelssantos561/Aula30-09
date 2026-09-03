from django.shortcuts import render

def app(request):
    return render(request, 'app.html')

def carrinho(request):
    return render(request, 'carrinho.html')

def painel(request):
    return render(request, 'painel.html')