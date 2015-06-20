# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_app', '0002_customer_order_order_product_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='shopify_app.Product', through='shopify_app.Order_Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='orders',
            field=models.ManyToManyField(to='shopify_app.Order', through='shopify_app.Order_Product'),
        ),
        migrations.AlterField(
            model_name='order_product',
            name='order',
            field=models.ForeignKey(to='shopify_app.Order'),
        ),
        migrations.AlterField(
            model_name='order_product',
            name='product',
            field=models.ForeignKey(to='shopify_app.Product'),
        ),
    ]
