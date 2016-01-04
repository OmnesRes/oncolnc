# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pan_cancer', '0004_auto_20151231_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='BLCA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='BRCA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='CESC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='COAD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='GBM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='HNSC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='KIRP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='LAML',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='LGG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='LIHC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='LUAD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='LUSC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='OV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='SKCM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='STAD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=10)),
                ('Cox', models.CharField(max_length=10)),
                ('p_value', models.CharField(max_length=10)),
                ('fdr', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
                ('expression', models.TextField(default=b'empty')),
            ],
        ),
    ]
