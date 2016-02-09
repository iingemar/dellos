# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.IntegerField(default=0, null=True, blank=True)),
                ('name', models.CharField(max_length=300, null=True, blank=True)),
                ('comment', models.CharField(max_length=300, null=True, blank=True)),
                ('price', models.IntegerField(default=0, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.IntegerField(default=0, null=True, blank=True)),
                ('name', models.CharField(max_length=300, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(blank=True, to='app_name.FoodCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='ingredients',
            field=models.ManyToManyField(to='app_name.Ingredient', null=True, blank=True),
            preserve_default=True,
        ),
    ]
