# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pan_cancer', '0003_cancers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancers',
            name='data',
        ),
        migrations.DeleteModel(
            name='CANCERS',
        ),
    ]
