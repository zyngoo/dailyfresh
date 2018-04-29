# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodinfo',
            name='gclick',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='goodinfo',
            name='gcontent',
            field=tinymce.models.HTMLField(default=b'\xe8\xbf\x99\xe6\x98\xaf\xe4\xb8\x80\xe6\xae\xb5\xe8\x91\xa1\xe8\x90\x84\xe7\x9a\x84\xe4\xbb\x8b\xe7\xbb\x8d!'),
        ),
        migrations.AlterField(
            model_name='goodinfo',
            name='gjianjie',
            field=models.CharField(default=b'\xe8\xbf\x99\xe6\x98\xaf\xe4\xb8\x80\xe6\xae\xb5\xe8\x91\xa1\xe8\x90\x84\xe7\x9a\x84\xe7\xae\x80\xe4\xbb\x8b!', max_length=200),
        ),
        migrations.AlterField(
            model_name='goodinfo',
            name='gkucun',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='goodinfo',
            name='gprice',
            field=models.DecimalField(default=38, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='goodinfo',
            name='gtitle',
            field=models.CharField(default=b'\xe7\xbb\xb4\xe5\xa4\x9a\xe5\x88\xa9\xe4\xba\x9a\xe8\x91\xa1\xe8\x90\x84', max_length=20),
        ),
    ]
