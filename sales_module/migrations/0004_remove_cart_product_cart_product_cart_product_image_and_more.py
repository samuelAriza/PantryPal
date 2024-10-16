# Generated by Django 5.1.1 on 2024-10-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_module', '0003_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_product',
            name='cart_product',
        ),
        migrations.AddField(
            model_name='cart_product',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='cart_product',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='cart_product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
