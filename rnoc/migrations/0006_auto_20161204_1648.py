# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0005_mll_ngay_gio_comment_cuoi_cung'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='Name_khong_dau',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='mll',
            name='ngay_gio_comment_cuoi_cung',
            field=models.DateTimeField(null=True, verbose_name='Ng\xe0y gi\u1edd comment cu\u1ed1i c\xf9ng', blank=True),
        ),
    ]
