# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rnoc', '0013_auto_20161229_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='NhaTram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(unique=True, max_length=80)),
                ('ngay_gio_tao', models.DateTimeField(default=datetime.datetime.now, verbose_name='Ng\xe0y gi\u1edd t\u1ea1o', blank=True)),
                ('ngay_gio_sua', models.DateTimeField(null=True, verbose_name='Ng\xe0y gi\u1edd s\u1eeda cu\u1ed1i c\xf9ng', blank=True)),
                ('nguoi_sua_cuoi_cung', models.ForeignKey(related_name='user_nguoi_sua_dot_nhatram_set', verbose_name='ng\u01b0\u1eddi s\u1eeda cu\u1ed1i c\xf9ng', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('nguoi_tao', models.ForeignKey(related_name='user_nguoi_tao_dot_nhatram_set', verbose_name='Ng\u01b0\u1eddi t\u1ea1o', blank=True, to=settings.AUTH_USER_MODEL)),
                ('tram_2g1', models.ForeignKey(related_name='Nhatramdottram_2g1', blank=True, to='rnoc.Tram', null=True)),
                ('tram_2g2', models.ForeignKey(related_name='Nhatramdottram_2g2', blank=True, to='rnoc.Tram', null=True)),
                ('tram_3g1', models.ForeignKey(related_name='Nhatramdottram_3g1', blank=True, to='rnoc.Tram', null=True)),
                ('tram_3g2', models.ForeignKey(related_name='Nhatramdottram_3g2', blank=True, to='rnoc.Tram', null=True)),
            ],
        ),
    ]
