from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

def homepage(request):
    return render(request, 'productlist.html', {})

def product(request):
    return render(request, 'product.html', {})

class ShoesPageView(ListView):
    model = Post
    template_name = 'productlist.html'