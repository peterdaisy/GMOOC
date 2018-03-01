# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-11 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20171204_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(default='Banner/default.png', upload_to='static/Pic/Banner/%Y/%m', verbose_name='轮播图'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default='image/default.png', upload_to='static/Pic/image/%Y/%m', verbose_name='头像'),
        ),
    ]