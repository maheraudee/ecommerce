# Generated by Django 4.0.2 on 2022-05-06 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0011_alter_order_odate_alter_order_otime_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reserve',
        ),
        migrations.AlterField(
            model_name='order',
            name='odate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='otime',
            field=models.TimeField(blank=True),
        ),
    ]