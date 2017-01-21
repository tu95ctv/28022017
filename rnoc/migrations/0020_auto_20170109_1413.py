# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0019_auto_20170103_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracnghiem',
            name='cau_hoi',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
