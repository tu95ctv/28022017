# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0012_auto_20161224_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='tram',
            name='tan_so_3G',
            field=models.ForeignKey(blank=True, to='rnoc.TanSo3G', null=True),
        ),
        migrations.AlterField(
            model_name='tram',
            name='Site_type',
            field=models.ForeignKey(to='rnoc.SiteType', blank=True),
        ),
    ]
