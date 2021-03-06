# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-14 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20171113_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(default='Banner/default.png', upload_to='Pic/Banner/%Y/%m', verbose_name='轮播图'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='adress',
            field=models.CharField(default='', max_length=100, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='女', max_length=6, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default='image/default.png', upload_to='Pic/image/%Y/%m', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='电话'),
        ),
    ]
