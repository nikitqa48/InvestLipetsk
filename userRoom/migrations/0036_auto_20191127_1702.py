# Generated by Django 2.2.6 on 2019-11-27 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userRoom', '0035_message_data_send'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message_to',
            new_name='moderator',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='message_from',
            new_name='user',
        ),
    ]
