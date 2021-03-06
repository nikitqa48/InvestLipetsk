# Generated by Django 2.2.6 on 2019-11-28 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Телефон')),
                ('first_name', models.CharField(blank=True, max_length=20, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, max_length=20, verbose_name='Фамилия')),
                ('last_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(blank=True, max_length=40, null=True, verbose_name='Почта')),
                ('organisation', models.CharField(blank=True, max_length=30, null=True, verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_send', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/userRoom/img')),
                ('news_data', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('news_header', models.CharField(blank=True, max_length=40, null=True, verbose_name='Заголовок новости')),
                ('news_text', models.TextField(blank=True, null=True, verbose_name='Текст новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Почта')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Телефон')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя региона')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
            },
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30, verbose_name='Наименование проекта')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание проекта')),
                ('industry', models.CharField(blank=True, max_length=30, null=True, verbose_name='Вид деятельности')),
                ('data_send', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('cost', models.CharField(blank=True, max_length=40, null=True, verbose_name='Стоимость проекта')),
                ('square', models.CharField(blank=True, max_length=40, null=True, verbose_name='Площадь земельного участка')),
                ('work', models.CharField(blank=True, max_length=5, null=True, verbose_name='Колличество рабочих')),
                ('status', models.CharField(blank=True, choices=[('0', 'В рассмотрении'), ('1', 'В сопровождении'), ('2', 'Завершено')], default='0', max_length=5, null=True, verbose_name='статус')),
                ('time', models.DateField(blank=True, null=True, verbose_name='Время исполения заявки')),
                ('profiles', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userRoom.Profile')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(blank=True, default=1, max_length=20, null=True, verbose_name='Имя организации')),
                ('contacts', models.CharField(blank=True, default=1, max_length=40, null=True, verbose_name='Контакты организации')),
                ('industry', models.CharField(blank=True, default=1, max_length=30, null=True, verbose_name='Вид деятельности')),
                ('profile_organisation', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='userRoom.Profile')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'Не прочитано'), ('1', 'прочитано')], default='0', max_length=3, null=True, verbose_name='Статус')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
                ('data_send', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('moderator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userRoom.Manager')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.AddField(
            model_name='manager',
            name='zayavka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userRoom.Statement'),
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('territory', models.CharField(blank=True, max_length=30, null=True, verbose_name='Территория региона')),
                ('invest', models.CharField(blank=True, max_length=30, null=True, verbose_name='Инвестиции в капитал')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userRoom.Region')),
            ],
            options={
                'verbose_name': 'Информацию',
                'verbose_name_plural': 'Информация',
            },
        ),
    ]
