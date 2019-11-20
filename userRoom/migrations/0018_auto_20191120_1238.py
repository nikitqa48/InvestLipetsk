# Generated by Django 2.2.6 on 2019-11-20 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userRoom', '0017_auto_20191119_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='statement',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'неактивна'), (1, 'В сопровождении'), (2, 'Завершено')], default=0, null=True),
        ),
    ]
