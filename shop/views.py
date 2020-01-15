from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.shortcuts import render, get_object_or_404

def homepage(request):
    return render(request, 'productlist.html', {})

def product_detail(request, pk):
    # return render(request, 'product.html', {})
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'product.html', {'post': post})

def product(request):
    return render(request, 'product.html', {})


class ShoesPageView(ListView):
    model = Post
    template_name = 'productlist.html'

