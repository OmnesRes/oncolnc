# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ALL_GENE_IDS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene_id', models.CharField(max_length=22)),
                ('all_data', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='ALL_GENES',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=22)),
                ('all_data', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='lncRNA_PATIENTS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cancer', models.CharField(max_length=4)),
                ('clinical', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='miRNA_PATIENTS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cancer', models.CharField(max_length=4)),
                ('clinical', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='mRNA_PATIENTS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cancer', models.CharField(max_length=4)),
                ('clinical', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='ONCOLNC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cancer', models.CharField(max_length=4)),
                ('gene', models.CharField(max_length=22)),
                ('gene_id', models.CharField(max_length=12)),
                ('Cox', models.CharField(max_length=6)),
                ('p_value', models.CharField(max_length=7)),
                ('fdr', models.CharField(max_length=7)),
                ('rank', models.CharField(max_length=6)),
                ('mean', models.CharField(max_length=6)),
                ('median', models.CharField(max_length=6)),
                ('expression', models.TextField(default=b'empty')),
                ('species', models.CharField(max_length=6)),
            ],
        ),
    ]
