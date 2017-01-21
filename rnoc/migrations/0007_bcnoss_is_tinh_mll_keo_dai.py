# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0006_auto_20161204_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='bcnoss',
            name='is_tinh_mll_keo_dai',
            field=models.BooleanField(default=False),
        ),
    ]
