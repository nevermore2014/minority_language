# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0002_auto_20150513_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'date published'),
        ),
    ]
