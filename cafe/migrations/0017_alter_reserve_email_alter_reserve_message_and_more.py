# Generated by Django 4.0.2 on 2022-05-06 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0016_alter_reserve_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='email',
            field=models.EmailField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='message',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
