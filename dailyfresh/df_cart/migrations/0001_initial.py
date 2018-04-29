# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0002_auto_20180420_1331'),
        ('df_goods', '0002_auto_20180423_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=0)),
                ('goods', models.ForeignKey(to='df_goods.GoodInfo')),
                ('user', models.ForeignKey(to='df_user.UserInfo')),
            ],
        ),
    ]
