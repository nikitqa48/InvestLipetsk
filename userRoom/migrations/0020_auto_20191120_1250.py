# Generated by Django 2.2.6 on 2019-11-20 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRoom', '0019_auto_20191120_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='status',
            field=models.CharField(choices=[('0', 'неактивна'), ('1', 'В сопровождении'), ('2', 'Завершено')], default='0', max_length=5, null=True),
        ),
    ]
