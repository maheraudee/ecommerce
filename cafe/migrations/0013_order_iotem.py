# Generated by Django 4.0.2 on 2022-05-06 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0012_delete_reserve_alter_order_odate_alter_order_otime'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='iotem',
            field=models.ManyToManyField(to='cafe.Item'),
        ),
    ]