# Generated by Django 4.2.3 on 2023-08-06 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodging', '0004_lodgingscrap_createdat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lodgingscrap',
            name='createdAt',
        ),
        migrations.AddField(
            model_name='review',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 8, 6, 17, 2, 46, 448508, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
