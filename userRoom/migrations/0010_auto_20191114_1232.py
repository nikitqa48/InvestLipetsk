# Generated by Django 2.2.6 on 2019-11-14 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRoom', '0009_profile_second_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Телефон'),
        ),
    ]