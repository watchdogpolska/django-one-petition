# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import swapper


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0005_remove_signature_location'),
        swapper.dependency('petition', 'Petition')
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('thank_you', models.TextField(verbose_name='Thank you text')),
                ('public', models.BooleanField(default=False, verbose_name='Public available')),
                ('main', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Petition',
                'verbose_name_plural': 'Petition',
                'swappable': swapper.swappable_setting('petition', 'Petition'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='signature',
            options={'verbose_name': 'Signature', 'verbose_name_plural': 'Signatures'},
        ),
        migrations.AddField(
            model_name='signature',
            name='petition',
            field=models.ForeignKey(default=1, verbose_name='Petition',
                                    to=swapper.get_model_name('petition', 'Petition')),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signature',
            name='lat',
            field=models.FloatField(null=True, verbose_name='Latitude', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signature',
            name='lng',
            field=models.FloatField(null=True, verbose_name='Longitude', blank=True),
            preserve_default=True,
        ),
    ]
