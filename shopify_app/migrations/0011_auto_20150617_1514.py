# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_app', '0010_auto_20150617_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='store',
            field=models.ForeignKey(related_name='products', to='shopify_app.Store'),
        ),
    ]
