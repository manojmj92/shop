# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_app', '0008_auto_20150617_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_product',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
