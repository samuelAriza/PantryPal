# Generated by Django 5.1.1 on 2024-11-10 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_module', '0008_alter_product_inventory_pick_up_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pick_up_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product_inventory',
            name='pick_up_address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
