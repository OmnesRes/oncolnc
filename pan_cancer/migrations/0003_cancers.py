# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pan_cancer', '0002_auto_20151231_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='CANCERS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cancer', models.CharField(max_length=10)),
                ('data', models.ForeignKey(to='pan_cancer.KIRC')),
            ],
        ),
    ]
