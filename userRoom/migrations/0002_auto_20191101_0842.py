# Generated by Django 2.2.6 on 2019-11-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRoom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Рассмотрение'), (1, 'Неактивна'), (2, 'Реализация'), (3, 'Завершено')], default=0, null=True),
        ),
    ]