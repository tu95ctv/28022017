# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0011_tram_macro_or_ibs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tram',
            name='Site_Name_1',
            field=models.CharField(default='abc', unique=True, max_length=80),
            preserve_default=False,
        ),
    ]
