# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0007_bcnoss_is_tinh_mll_keo_dai'),
    ]

    operations = [
        migrations.AddField(
            model_name='mll',
            name='type_2g_or_3g',
            field=models.ForeignKey(verbose_name='Tr\u1ea1ng th\xe1i', blank=True, to='rnoc.BTSType', null=True),
        ),
        migrations.AlterField(
            model_name='bcnoss',
            name='is_tinh_mll_keo_dai',
            field=models.BooleanField(default=False, verbose_name='T\xednh mll k\xe9o d\xe0i'),
        ),
    ]
