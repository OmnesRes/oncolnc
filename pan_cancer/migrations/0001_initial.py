# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KIRC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
            ],
        ),
    ]
