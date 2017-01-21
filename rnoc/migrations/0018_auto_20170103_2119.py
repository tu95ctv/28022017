# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0017_bcnoss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='Name',
            field=models.CharField(unique=True, max_length=130),
        ),
        migrations.AlterField(
            model_name='thietbi',
            name='Name',
            field=models.CharField(unique=True, max_length=120),
        ),
    ]
