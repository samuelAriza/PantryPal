# Generated by Django 5.0.7 on 2024-08-31 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
