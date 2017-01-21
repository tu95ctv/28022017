# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0002_auto_20161130_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='bcnoss',
            name='kien_nghi_de_xuat',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
