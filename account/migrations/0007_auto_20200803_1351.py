# Generated by Django 3.0 on 2020-08-03 08:21

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200802_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=account.models.get_resume_name, verbose_name='resume'),
        ),
    ]
