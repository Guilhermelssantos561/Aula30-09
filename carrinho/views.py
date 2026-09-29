from django.shortcuts import render
from django.shortcuts import redirect

def remover_item(request, item_id):
    carrinho = request.session.get('carrinho', {})
    if str(item_id) in carrinho:
        del carrinho[str(item_id)]
        request.session['carrinho'] = carrinho
    return redirect('carrinho')

def carrinho(request):
    return render(request, 'carrinho.html')

# carrinho/views.py

def checkout_dados(request):
    return render(request, 'checkout_dados.html')


from django.shortcuts import render

def checkout_dados(request):
    return render(request, 'checkout_dados.html')