# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0004_auto_20161204_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='mll',
            name='ngay_gio_comment_cuoi_cung',
            field=models.DateTimeField(null=True, verbose_name='Ng\xe0y gi\u1edd s\u1eeda cu\u1ed1i c\xf9ng', blank=True),
        ),
    ]
