# Generated by Django 3.1.6 on 2010-12-31 21:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20210302_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2011, 1, 1, 0, 8, 47, 288870)),
        ),
    ]
