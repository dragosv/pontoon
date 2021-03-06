# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 23:20
from __future__ import unicode_literals

from django.db import migrations, models
import pontoon.base.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0078_auto_20170209_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locale',
            name='cldr_plurals',
            field=models.CharField(blank=True, help_text=b'\n        A comma separated list of <a href="http://www.unicode.org/cldr/charts/dev/supplemental/language_plural_rules.html">CLDR plural rules</a>,\n        where 0 represents zero, 1 one, 2 two, 3 few, 4 many, and 5 other.\n        E.g. 1,5\n        ', max_length=11, validators=[pontoon.base.models.validate_cldr], verbose_name=b'CLDR Plurals'),
        ),
    ]
