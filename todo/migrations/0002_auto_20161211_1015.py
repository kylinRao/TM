# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-11 10:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='user_ame',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='remind_receiver_email',
        ),
    ]
