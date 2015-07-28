# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import swapper


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0006_auto_20150728_0005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='petition',
            options={},
        ),
        migrations.AlterField(
            model_name='petition',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signature',
            name='petition',
            field=models.ForeignKey(verbose_name='Petition', to=swapper.get_model_name('petition', 'Petition')),
            preserve_default=True,
        ),
    ]
