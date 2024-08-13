from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'template.html')
def add_products(request):
    products = Product.objects.all()
    return render(request, 'add.html', {'products': products})

