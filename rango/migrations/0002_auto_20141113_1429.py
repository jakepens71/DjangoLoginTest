# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'profile_images'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.URLField(default=True, blank=True),
            preserve_default=False,
        ),
    ]
