from django.urls import path
from . import views

app_name = "sales_module"

urlpatterns = [
    path('sales_module/', views.sales_module, name='sales_module'),
    path('publish_product/', views.publish_product, name='publish_product'),
    path('add_publish_product/', views.add_publish_product, name='add_publish_product'),
]