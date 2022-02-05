# Generated by Django 4.0.2 on 2022-02-01 21:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='mitem',
            field=models.ManyToManyField(to='cafe.Item'),
        ),
        migrations.AlterField(
            model_name='order',
            name='odate',
            field=models.DateField(blank=True, default=datetime.date(2022, 2, 2)),
        ),
        migrations.AlterField(
            model_name='order',
            name='otime',
            field=models.TimeField(blank=True, default=datetime.time(0, 13, 37, 618278)),
        ),
    ]