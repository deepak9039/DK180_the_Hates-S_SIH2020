# Generated by Django 3.0 on 2020-08-01 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20200802_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='timestamp_str',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
