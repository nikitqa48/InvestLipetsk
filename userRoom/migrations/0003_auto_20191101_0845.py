# Generated by Django 2.2.6 on 2019-11-01 05:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userRoom', '0002_auto_20191101_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='data_send',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='statement',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'неактивна'), (1, 'В сопровождении'), (2, 'Реализация'), (3, 'Завершено')], default=0, null=True),
        ),
    ]
