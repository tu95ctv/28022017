# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0003_bcnoss_kien_nghi_de_xuat'),
    ]

    operations = [
        migrations.AddField(
            model_name='mll',
            name='chap_chon',
            field=models.BooleanField(default=False, verbose_name='Ch\u1eadp ch\u1eddn'),
        ),
        migrations.AlterField(
            model_name='bcnoss',
            name='kien_nghi_de_xuat',
            field=models.CharField(max_length=500, null=True, verbose_name='Ki\u1ebfn ngh\u1ecb \u0111\u1ec1 xu\u1ea5t', blank=True),
        ),
    ]
