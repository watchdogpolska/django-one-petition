# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0003_auto_20150415_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='newsletter',
            field=models.BooleanField(default=True, verbose_name='Newsletter acceptation'),
            preserve_default=True,
        ),
    ]
