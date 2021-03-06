from django.urls import path
from . import views
from .views import ShoesPageView

urlpatterns = [
    # path('', views.homepage, name='home'),
    path('product', views.product, name='product'),
    path('', ShoesPageView.as_view(), name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]