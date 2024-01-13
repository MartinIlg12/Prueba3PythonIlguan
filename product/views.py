from django.shortcuts import render
from .models import Product

# Create your views here.
def product(request):
    product = Product.objects.all()
    return render(request,'product/product.html',{'product':product})