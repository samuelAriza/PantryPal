from django.shortcuts import render
from django.http import HttpResponse
from sale.models import PublishProduct

# Create your views here.

def home(request):
    products = PublishProduct.objects.filter(product_type="sale")
    return render (request, 'template_sale.html', {"products":products})