# Generated by Django 2.2.6 on 2019-10-18 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRoom', '0010_profile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.AddField(
            model_name='profile',
            name='name_profile',
            field=models.CharField(default=12, max_length=20, verbose_name='Ваше имя'),
        ),
    ]