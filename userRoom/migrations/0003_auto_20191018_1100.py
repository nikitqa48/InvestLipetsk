# Generated by Django 2.2.6 on 2019-10-18 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userRoom', '0002_auto_20191018_1059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisation',
            options={'verbose_name': 'Организация'},
        ),
        migrations.AlterModelOptions(
            name='statement',
            options={'verbose_name': 'Заяка'},
        ),
    ]