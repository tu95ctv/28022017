# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0008_auto_20161210_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='mll',
            name='brand',
            field=models.ForeignKey(verbose_name='Brand', blank=True, to='rnoc.Brand', null=True),
        ),
        migrations.AlterField(
            model_name='mll',
            name='type_2g_or_3g',
            field=models.ForeignKey(verbose_name='2G or 3G', blank=True, to='rnoc.BTSType', null=True),
        ),
    ]
