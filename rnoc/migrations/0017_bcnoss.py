# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnoc', '0016_auto_20170103_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='BCNOSS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object', models.CharField(max_length=50, verbose_name='\u0110\u1ed1i t\u01b0\u1ee3ng')),
                ('gio_mat', models.DateTimeField(verbose_name='Gi\u1edd m\u1ea5t')),
                ('gio_tot', models.DateTimeField(null=True, verbose_name='gi\u1edd t\u1ed1t', blank=True)),
                ('code_loi', models.IntegerField()),
                ('vnp_comment', models.CharField(max_length=500)),
                ('gio_canh_bao_ac', models.DateTimeField(null=True, verbose_name='gi\u1edd canh bao AC', blank=True)),
                ('tong_thoi_gian', models.IntegerField(null=True, verbose_name='t\u1ed5ng th\u1eddi gian', blank=True)),
                ('kien_nghi_de_xuat', models.CharField(max_length=500, null=True, verbose_name='Ki\u1ebfn ngh\u1ecb \u0111\u1ec1 xu\u1ea5t', blank=True)),
                ('is_tinh_mll_keo_dai', models.BooleanField(default=False, verbose_name='T\xednh mll k\xe9o d\xe0i')),
                ('BSC_or_RNC', models.ForeignKey(blank=True, to='rnoc.BSCRNC', null=True)),
                ('BTS_Type', models.ForeignKey(verbose_name='2G,3G or 4G', blank=True, to='rnoc.BTSType', null=True)),
                ('BTS_thiet_bi', models.ForeignKey(verbose_name='Nh\xe0 s\u1ea3n xu\u1ea5t', blank=True, to='rnoc.ThietBi', null=True)),
                ('tinh', models.ForeignKey(verbose_name='T\u1ec9nh', to='rnoc.Tinh')),
            ],
        ),
    ]
