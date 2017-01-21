# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0014_nhatram'),
    ]

    operations = [
        migrations.AddField(
            model_name='tram',
            name='nha_tram',
            field=models.ForeignKey(to='rnoc.NhaTram', null=True),
        ),
    ]
