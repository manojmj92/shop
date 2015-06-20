# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_app', '0005_auto_20150613_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_product',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
