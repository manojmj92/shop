# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('api_key', models.CharField(max_length=50)),
                ('shared_secret', models.CharField(max_length=50)),
                ('permissions', models.CharField(max_length=100)),
                ('redirect_url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('access_token', models.CharField(max_length=50)),
            ],
        ),
    ]
