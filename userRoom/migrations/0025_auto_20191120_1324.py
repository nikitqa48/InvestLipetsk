# Generated by Django 2.2.6 on 2019-11-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRoom', '0024_auto_20191120_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='status',
            field=models.CharField(blank=True, choices=[('0', 'неактивна'), ('1', 'В сопровождении'), ('2', 'Завершено')], max_length=5, null=True, verbose_name='статус'),
        ),
    ]
