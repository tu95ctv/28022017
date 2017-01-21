# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0009_auto_20161210_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Name',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
    ]
