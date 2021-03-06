# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-11 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0008_vacuum_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusupdate',
            name='previous_status',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Draft'), (2, 'Submitted'), (3, 'Reviewed'), (4, 'Public'), (5, 'Rejected'), (6, 'Inactive')], null=True),
        ),
        migrations.AlterField(
            model_name='mailpreferences',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('es', 'Spanish'), ('ru', 'Russian'), ('km', 'Khmer'), ('lo', 'Lao'), ('ar', 'Arabic'), ('pt', 'Portuguese'), ('af', 'Afrikaans'), ('th', 'Thai')], default='en', max_length=2),
        ),
    ]
