from django.shortcuts import render

def homepage(request):
    return render(request, 'productlist.html', {})

def product(request):
    return render(request, 'product.html', {})
