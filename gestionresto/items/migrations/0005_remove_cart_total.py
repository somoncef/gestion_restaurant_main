# Generated by Django 4.2.1 on 2023-06-04 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_cart_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
    ]
