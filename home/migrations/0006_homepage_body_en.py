# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-01 21:28
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_homepage_body_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
    ]
