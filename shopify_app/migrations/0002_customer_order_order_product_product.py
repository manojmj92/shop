# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('store', models.ForeignKey(related_name='customer', to='shopify_app.Store')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('customer', models.ForeignKey(related_name='order', to='shopify_app.Customer')),
                ('store', models.ForeignKey(related_name='order', to='shopify_app.Store')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.ForeignKey(related_name='order_of_product', to='shopify_app.Order')),
                ('product', models.ForeignKey(related_name='product_of_order', to='shopify_app.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('store', models.ForeignKey(related_name='product', to='shopify_app.Store')),
            ],
        ),
    ]
