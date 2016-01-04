# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pan_cancer', '0005_blca_brca_cesc_coad_gbm_hnsc_kirp_laml_lgg_lihc_luad_lusc_ov_skcm_stad'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BLCA',
        ),
    ]
