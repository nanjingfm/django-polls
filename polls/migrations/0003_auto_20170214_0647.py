# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170214_0602'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='desc_text',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='\u8c03\u67e5\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='question',
            name='img',
            field=models.ImageField(blank=True, default='', upload_to='polls/img/', verbose_name='\u56fe\u7247\u5730\u5740'),
        ),
    ]
