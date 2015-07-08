# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=64)),
                ('uploaded', models.DateTimeField(auto_now=True)),
                ('content_type', models.CharField(max_length=64)),
                ('size', models.BigIntegerField(null=True)),
                ('thumbnails', django_pgjson.fields.JsonBField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django_pgjson.fields.JsonBField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.CharField(default=uuid.uuid4, max_length=64)),
                ('code', models.CharField(default='', max_length=64)),
                ('blocked', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Pending'), (3, 'Approved'), (4, 'Rejected')])),
                ('version', models.IntegerField()),
                ('configurations', models.ManyToManyField(to='configuration.Configuration')),
            ],
            options={
                'ordering': ['-updated'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionnaireLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Pending'), (3, 'Approved'), (4, 'Rejected')])),
                ('to_status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Pending'), (3, 'Approved'), (4, 'Rejected')])),
                ('from_questionnaire', models.ForeignKey(to='questionnaire.Questionnaire', related_name='from_questionnaire')),
                ('to_questionnaire', models.ForeignKey(to='questionnaire.Questionnaire', related_name='to_questionnaire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionnaireMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionnaire', models.ForeignKey(to='questionnaire.Questionnaire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionnaireRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(unique=True, max_length=63)),
                ('description', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionnaireTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en', 'English'), ('es', 'Spanish')], max_length=63)),
                ('original_language', models.BooleanField(default=False)),
                ('questionnaire', models.ForeignKey(to='questionnaire.Questionnaire')),
            ],
            options={
                'ordering': ['-original_language'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='questionnairemembership',
            name='role',
            field=models.ForeignKey(to='questionnaire.QuestionnaireRole'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='questionnairemembership',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='links',
            field=models.ManyToManyField(null=True, to='questionnaire.Questionnaire', related_name='linked_to+', through='questionnaire.QuestionnaireLink'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='members',
            field=models.ManyToManyField(through='questionnaire.QuestionnaireMembership', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
