# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BLCA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='BRCA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='CESC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='COAD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='ESCA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='GBM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='HNSC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='KIRC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='KIRP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='LAML',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='LGG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='LIHC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='lncRNA_PATIENTS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cancer', models.CharField(max_length=4)),
                ('clinical', models.TextField(default=b'empty')),
            ],
        ),
        migrations.CreateModel(
            name='LUAD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='LUSC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            name='OV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='PAAD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='READ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='SARC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='SKCM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='STAD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='UCEC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
