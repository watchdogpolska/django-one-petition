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
            options={'swappable': swapper.swappable_setting('petition', 'Petition')},
        ),
    ]
