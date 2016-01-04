# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pan_cancer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PATIENTS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cancer', models.CharField(max_length=10)),
                ('clinical', models.TextField(default=b'empty')),
            ],
        ),
        migrations.AddField(
            model_name='kirc',
            name='expression',
            field=models.TextField(default=b'empty'),
        ),
    ]
