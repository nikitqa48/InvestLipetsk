# Generated by Django 2.2.6 on 2019-11-07 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userRoom', '0003_auto_20191101_0845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'Куратор', 'verbose_name_plural': 'Кураторы'},
        ),
    ]