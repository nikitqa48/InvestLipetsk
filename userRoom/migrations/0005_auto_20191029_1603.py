# Generated by Django 2.2.6 on 2019-10-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRoom', '0004_auto_20191025_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='cost',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Стоимость проекта'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание проекта'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='industry',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Вид деятельности'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='project_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Наименование проекта'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='square',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Площадь земельного участка'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='work',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Колличество рабочих'),
        ),
    ]
