# Generated by Django 4.0.2 on 2022-05-04 07:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0008_alter_order_otime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='otime',
            field=models.TimeField(blank=True, default=datetime.time(10, 6, 39, 122502)),
        ),
    ]
