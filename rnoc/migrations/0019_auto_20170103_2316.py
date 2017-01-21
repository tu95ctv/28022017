# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0018_auto_20170103_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bcnoss',
            name='is_tinh_mll_keo_dai',
        ),
        migrations.AddField(
            model_name='bcnoss',
            name='is_khong_tinh_mll_keo_dai',
            field=models.BooleanField(default=False, verbose_name='Kh\xf4ng T\xednh mll k\xe9o d\xe0i'),
        ),
    ]
