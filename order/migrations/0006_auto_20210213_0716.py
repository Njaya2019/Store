# Generated by Django 3.1.6 on 2021-02-13 04:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20210213_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime),
        ),
    ]
