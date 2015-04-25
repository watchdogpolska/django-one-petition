# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0002_signature_telephone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signature',
            name='name',
        ),
        migrations.AddField(
            model_name='signature',
            name='first_name',
            field=models.CharField(default='Gall', max_length=100, verbose_name='First name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signature',
            name='second_name',
            field=models.CharField(default='Anonim', max_length=100, verbose_name='Second name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signature',
            name='city',
            field=models.CharField(max_length=100, verbose_name='City'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signature',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created on'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signature',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='E-mail'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signature',
            name='lat',
            field=models.FloatField(null=True, verbose_name='Latitude'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signature',
            name='lng',
            field=models.FloatField(null=True, verbose_name='Longitude'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signature',
            name='location',
            field=models.CharField(max_length=150, verbose_name='Location'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signature',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified on'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signature',
            name='telephone',
            field=models.CharField(max_length=12, null=True, verbose_name='Telephone', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signature',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Visible'),
            preserve_default=True,
        ),
    ]
