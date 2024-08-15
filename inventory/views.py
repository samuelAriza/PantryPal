from django.shortcuts import render, HttpResponse, redirect
from .models import Product
from django.contrib import messages
from sale.models import PublishProduct 
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home_restaurant_chain(request):
    return render(request, 'template_inventory.html')

def show_product(request):
    products = Product.objects.all()
    return render(request, 'add_product.html', {'products': products})

def add_product(request):
    name = request.POST['input_name']
    category = request.POST['input_category']
    total_quantity = request.POST['input_total_quantity']
    sale_price = request.POST['input_sale_price']

    product = Product.objects.create(name=name, category=category, total_quantity=total_quantity, sale_price=sale_price)

    return redirect('inventory')
def delete_product(request, id):
    product = Product.objects.get(id=id).delete()
    return redirect('inventory')

def before_edit_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'edit_product.html', {'product': product})

def edit_product(request):
    id = request.POST['input_id']
    name = request.POST['input_name']
    category = request.POST['input_category']
    total_quantity = request.POST['input_total_quantity']
    sale_price = request.POST['input_sale_price']

    product = Product.objects.get(id=id)
    product.name = name 
    product.category = category
    product.total_quantity = total_quantity
    product.sale_price = sale_price
    product.save()

    return redirect('inventory')

#Views from publishing
def add_publish_product(request):
    if request.method == "POST":
        product = Product.objects.get(id = int(request.POST.get('product_name')))
        print("-------------------")
        name = product.name
        print(name)
        publish_type = request.POST.get('type')
        quantity = request.POST.get('quantity')
        publish_price = request.POST.get('price')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        image = request.FILES['product_image']

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        print("################################")
        print(uploaded_file_url)
        print("################################")
        publish_details = {
            "name": name,
            "publish_type": publish_type, 
            "quantity":int(quantity),
            "publish_price":publish_price,
            "start_date":start_date, 
            "end_date":end_date
        }

        PublishProduct.objects.create(
            name = name,
            product_type = publish_type,
            quantity = int(quantity),
            publish_price = publish_price,
            start_date = start_date,
            end_date = end_date,
            img = uploaded_file_url,
        )

        product.total_quantity = product.total_quantity - int(quantity)
        product.save()

        print(publish_details)
        print("-------------------")

    return redirect('inventory')







