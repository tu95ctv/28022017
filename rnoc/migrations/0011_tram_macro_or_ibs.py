# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0010_userprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tram',
            name='macro_or_ibs',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
