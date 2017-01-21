# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0015_tram_nha_tram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bcnoss',
            name='BSC_or_RNC',
        ),
        migrations.RemoveField(
            model_name='bcnoss',
            name='BTS_Type',
        ),
        migrations.RemoveField(
            model_name='bcnoss',
            name='BTS_thiet_bi',
        ),
        migrations.RemoveField(
            model_name='bcnoss',
            name='tinh',
        ),
        migrations.DeleteModel(
            name='BCNOSS',
        ),
    ]
