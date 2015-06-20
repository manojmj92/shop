# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_app', '0009_auto_20150617_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_product',
            name='order',
            field=models.ForeignKey(related_name='orders', to='shopify_app.Order'),
        ),
        migrations.AlterField(
            model_name='order_product',
            name='product',
            field=models.ForeignKey(related_name='products', to='shopify_app.Product'),
        ),
    ]
