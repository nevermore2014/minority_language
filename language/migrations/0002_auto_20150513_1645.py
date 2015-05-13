# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='quize_text',
        ),
        migrations.AddField(
            model_name='quiz',
            name='quize_text_chinese',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='quize_text_english',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='quize_text_portuguese',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
