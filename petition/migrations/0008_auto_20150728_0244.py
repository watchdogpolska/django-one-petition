# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0007_auto_20150728_0239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='signature',
            options={'swappable': swapper.swappable_setting('petition', 'Petition')},
        ),
    ]
