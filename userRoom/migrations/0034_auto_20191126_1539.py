# Generated by Django 2.2.6 on 2019-11-26 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userRoom', '0033_auto_20191126_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
