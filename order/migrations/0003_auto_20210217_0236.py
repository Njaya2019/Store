# Generated by Django 3.1.6 on 2021-02-16 23:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210214_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 17, 2, 36, 39, 829907)),
        ),
    ]
