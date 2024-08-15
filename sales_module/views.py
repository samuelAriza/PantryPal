from django.shortcuts import render, HttpResponse
from sales_module.models import sale_products

products_sale = []
products_donate = []

#Examples of products for apply publishing fucntion.
products = [
    {
        "id": 1,
        "name": "Cheddar Cheese",
        "category": "Dairy",
        "quantity": 50,
        "price": 5.99
    },
    {
        "id": 2,
        "name": "Olive Oil",
        "category": "Condiments",
        "quantity": 30,
        "price": 12.49
    },
    {
        "id": 3,
        "name": "Whole Wheat Bread",
        "category": "Bakery",
        "quantity": 100,
        "price": 3.49
    },
    {
        "id": 4,
        "name": "Ribeye Steak",
        "category": "Meat",
        "quantity": 20,
        "price": 24.99
    },
    {
        "id": 5,
        "name": "Romaine Lettuce",
        "category": "Vegetables",
        "quantity": 75,
        "price": 2.99
    }
]


# Create your views here.
def sales_module(request):
    return render(request, 'index.html', {"products":products})

def publish_product(request):
    return render(request, 'publish.html', {"products":products})

def add_publish_product(request):
    if request.method == "POST":
        print("-------------------")
        idr = request.POST.get('product_id')
        publish_type = request.POST.get('type')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        publish_details = {
            "idr":idr,
            "publish_type": publish_type, 
            "quantity":quantity,
            "price":price,
            "start_date":start_date, 
            "end_date":end_date
        }

        sale_products.objects.create(
            product_id = int(idr),
            product_type = publish_type,
            quantity = int(quantity),
            price = price,
            start_date = start_date,
            end_date = end_date,
        )

        if publish_type == "sale":
            products_sale.append(publish_details)
        else:
            products_donate.append(publish_details)

        print(products_sale)
        print("-------------------")

    return render(request, 'publish.html', {"products":products})

