# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-13 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171112_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(default='Banner/default.png', upload_to='Banner/%Y/%M', verbose_name='轮播图'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='生日日期'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y/%M', verbose_name='头像'),
        ),
    ]