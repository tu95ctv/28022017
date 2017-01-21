# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0020_auto_20170109_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bscrnc',
            name='ghi_chu',
            field=models.CharField(max_length=500, null=True, verbose_name='Ghi Ch\xfa', blank=True),
        ),
        migrations.AlterField(
            model_name='catruc',
            name='ghi_chu',
            field=models.CharField(max_length=500, null=True, verbose_name='Ghi Ch\xfa', blank=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='ghi_chu',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='diaban',
            name='ghi_chu',
            field=models.CharField(max_length=500, null=True, verbose_name='Ghi Ch\xfa', blank=True),
        ),
        migrations.AlterField(
            model_name='faultlibrary',
            name='ghi_chu',
            field=models.CharField(max_length=500, null=True, verbose_name='Ghi Ch\xfa', blank=True),
        ),
        migrations.AlterField(
            model_name='nguyennhan',
            name='ghi_chu',
            field=models.CharField(max_length=500, null=True, verbose_name='Ghi Ch\xfa', blank=True),
        ),
        migrations.AlterField(
            model_name='suco',
            name='ghi_chu',
            field=models.CharField(max_length=500, null=True, verbose_name='Ghi Ch\xfa', blank=True),
        ),
        migrations.AlterField(
            model_name='thaotaclienquan',
            name='ghi_chu',
            field=models.CharField(max_length=500, null=True, verbose_name='Ghi Ch\xfa', blank=True),
        ),
        migrations.AlterField(
            model_name='thietbi',
            name='ghi_chu',
            field=models.CharField(max_length=500, null=True, verbose_name='Ghi ch\xfa', blank=True),
        ),
        migrations.AlterField(
            model_name='tinh',
            name='ghi_chu',
            field=models.CharField(max_length=500, null=True, verbose_name='Ghi Ch\xfa', blank=True),
        ),
        migrations.AlterField(
            model_name='tram',
            name='ghi_chu_tram',
            field=models.CharField(max_length=500, null=True, verbose_name='Ghi Ch\xfa', blank=True),
        ),
        migrations.AlterField(
            model_name='trangthai',
            name='ghi_chu',
            field=models.CharField(max_length=500, null=True, verbose_name='Ghi Ch\xfa', blank=True),
        ),
    ]
