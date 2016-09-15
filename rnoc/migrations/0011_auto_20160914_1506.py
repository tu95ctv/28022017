# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rnoc', '0010_auto_20160718_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaBan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(unique=True, max_length=50)),
                ('Name_khong_dau', models.CharField(unique=True, max_length=50, blank=True)),
                ('ky_hieu', models.CharField(max_length=50)),
                ('ghi_chu', models.CharField(max_length=10000, null=True, verbose_name='Ghi Ch\xfa', blank=True)),
                ('so_luong_tram_2G', models.IntegerField(null=True, blank=True)),
                ('so_luong_tram_3G', models.IntegerField(null=True, blank=True)),
                ('ngay_gio_sua', models.DateTimeField(null=True, verbose_name='Ng\xe0y gi\u1edd s\u1eeda cu\u1ed1i c\xf9ng', blank=True)),
                ('ly_do_sua', models.CharField(max_length=100, verbose_name='L\xfd do s\u1eeda', blank=True)),
                ('nguoi_sua_cuoi_cung', models.ForeignKey(related_name='user_nguoi_sua_dot_diaban_set', verbose_name='ng\u01b0\u1eddi s\u1eeda cu\u1ed1i c\xf9ng', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='searchhistory',
            name='ghi_chu',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='doitac',
            name='ngay_gio_tao',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 15, 6, 6, 312000), verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True),
        ),
        migrations.AlterField(
            model_name='duan',
            name='ngay_gio_tao',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 15, 6, 6, 313000), verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True),
        ),
        migrations.AlterField(
            model_name='faultlibrary',
            name='ngay_gio_tao',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 15, 6, 6, 321000), verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True),
        ),
        migrations.AlterField(
            model_name='lenh',
            name='ngay_gio_tao',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 15, 6, 6, 322000), verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True),
        ),
        migrations.AlterField(
            model_name='mll',
            name='ngay_gio_tao',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 15, 6, 6, 332000), verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True),
        ),
        migrations.AlterField(
            model_name='nguyennhan',
            name='ngay_gio_tao',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 8, 6, 6, 317000, tzinfo=utc), verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True),
        ),
        migrations.AlterField(
            model_name='suco',
            name='ngay_gio_tao',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 8, 6, 6, 315000, tzinfo=utc), verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True),
        ),
        migrations.AlterField(
            model_name='thaotaclienquan',
            name='ngay_gio_tao',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 15, 6, 6, 320000), verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True),
        ),
        migrations.AlterField(
            model_name='thietbi',
            name='ngay_gio_tao',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 15, 6, 6, 311000), verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True),
        ),
        migrations.AlterField(
            model_name='tinh',
            name='dia_ban',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tinh',
            name='so_luong_tram_2G',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tinh',
            name='so_luong_tram_3G',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tinh',
            name='tong_so_tram',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tram',
            name='ngay_gio_tao',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 8, 6, 6, 328000, tzinfo=utc), verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True),
        ),
        migrations.AlterField(
            model_name='trangthai',
            name='ngay_gio_tao',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 15, 6, 6, 319000), verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ca_truc',
            field=models.ForeignKey(verbose_name='B\u1ea1n \u0111ang tr\u1ef1c ca n\xe0o?', blank=True, to='rnoc.CaTruc', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='color_code',
            field=models.CharField(max_length=15, null=True, verbose_name='M\xe0u hi\u1ec3n th\u1ecb', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='loc_ca',
            field=models.ManyToManyField(related_name='catruc_dot_userprofile_dot_set', verbose_name='B\u1ea1n mu\u1ed1n hi\xean th\u1ecb ca n\xe0o?', to='rnoc.CaTruc', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='so_dien_thoai',
            field=models.CharField(max_length=20, null=True, verbose_name='S\u1ed1 \u0111i\u1ec7n tho\u1ea1i', blank=True),
        ),
    ]
