from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    second_name = models.CharField('Фамилия', blank = True, null=True, max_length=50)
    last_name = models.CharField('Отчество', blank= True, null= True, max_length=50)
    email = models.CharField("Почта", blank=True, null=True, max_length=50)
    phone = models.CharField("Телефон", blank=True, null=True, max_length=30)
    # passport_serial = models.CharField('Серия паспорта', blank=True , null= True, max_length=100)
    # passport_number = models.CharField('Номер паспорта', blank = True, null = True, max_length=100)
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)




class Organisation(models.Model):
    profile_organisation = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True, blank = False,default=1)
    organisation_name = models.CharField("Имя организации", max_length=20, blank=True,null= True,default=1)
    contacts = models.CharField("Контакты организации", max_length=40, blank=True, null = True,default=1)
    industry = models.CharField("Вид деятельности", max_length=30, blank=True, null=True,default=1)

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"


    def __str__(self):
        return self.organisation_name



class Statement(models.Model):
    """ ЗАЯВКА """
    project_name = models.CharField("Наименование проекта", max_length=30,default=0)
    profiles = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField("Описание проекта", null = True, blank= True)
    industry = models.CharField('Вид деятельности', max_length=30, null = True, blank = True)
    data_send = models.DateTimeField(default=timezone.now, blank=False, null = True)
    cost = models.CharField("Стоимость проекта", max_length=40, null = True, blank = True)
    square = models.CharField("Площадь земельного участка", max_length=40, null = True, blank = True)
    work = models.CharField("Колличество рабочих", max_length=5,null = True, blank = True)
    ORDER_STATUS = (('0', 'неактивна'),('1', 'В сопровождении'), ('2', 'Завершено'))
    status = models.CharField('статус', choices=ORDER_STATUS, null=True , blank = True, default='0', max_length=5)
    time = models.DateField('Время исполения заявки', blank = True, null = True)

    def __str__(self):
        return self.project_name


    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


 
class Manager(models.Model):
    """ Привязка заявки к модератору """
    manager = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = False)
    zayavka = models.ForeignKey(Statement, on_delete=models.CASCADE, null = True, blank = False)
    data_send = models.DateTimeField(default=timezone.now, blank=False, null = True)
    class Meta:
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'
    def __str__(self):
        return self.manager.username



class News (models.Model):
    image = models.ImageField(upload_to='static/userRoom/img', height_field=None, width_field=None, max_length=100)
    news_data = models.DateTimeField(default=timezone.now, blank=False, null = True)
    news_header = models.CharField("Заголовок новости", max_length=40, null = True, blank = True)
    news_text = models.TextField('Текст новости', blank=True, null=True)
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    def __str__(self):
        return self.news_header


class Connection (models.Model):
    phone = models.CharField('Телефон',max_length=30,null=False, blank= True)
    first_name = models.CharField('Имя', max_length=20, null=False, blank=True)
    second_name = models.CharField('Фамилия', max_length=20, null=False, blank=True)
    last_name = models.CharField('Отчество', max_length=20, null=True, blank=True)
    email = models.EmailField('Почта', max_length=40, null=True, blank=True)
    organisation = models.CharField('Организация', max_length=30, null= True, blank=True)


    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связей'

    def __str__(self):
        return self.first_name



# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance, id=instance.id)
