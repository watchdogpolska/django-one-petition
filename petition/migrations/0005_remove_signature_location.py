# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0004_signature_newsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signature',
            name='location',
        ),
    ]
