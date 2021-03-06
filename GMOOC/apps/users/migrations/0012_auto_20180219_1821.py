# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-19 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180201_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifycode',
            name='send_type',
            field=models.CharField(choices=[('reguster', '注册'), ('forget', '忘记密码'), ('update', '更新邮箱')], max_length=20, verbose_name='发送类型'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default='image/def ault.png', upload_to='user_img/%Y/%m', verbose_name='头像'),
        ),
    ]
