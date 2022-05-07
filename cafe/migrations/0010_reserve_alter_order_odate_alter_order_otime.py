# Generated by Django 4.0.2 on 2022-05-06 04:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0009_alter_order_otime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('message', models.TimeField(default='', max_length=1000)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('nperson', models.IntegerField(default=1, max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='odate',
            field=models.DateField(blank=True, default=datetime.date(2022, 5, 6)),
        ),
        migrations.AlterField(
            model_name='order',
            name='otime',
            field=models.TimeField(blank=True, default=datetime.time(7, 0, 10, 768152)),
        ),
    ]