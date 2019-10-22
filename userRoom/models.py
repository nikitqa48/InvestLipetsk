from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField("Почта", blank=True, null=True, max_length=50)
    phone = models.CharField("Телефон", blank=True, null=False, max_length=30)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Organisation(models.Model):
    profile_organisation = models.ForeignKey(Profile, on_delete=models.CASCADE)
    contacts = models.CharField("Контакты организации", max_length=40, blank=True)
    organisation_name = models.CharField("Имя организации", max_length=20, blank=True)
    industry = models.CharField("Вид деятельности", max_length=30, blank=True)

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self):
        return self.organisation_name


class Statement(models.Model):
    statement_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_name = models.CharField("Наименование проекта", max_length=30)
    description = models.TextField("Описание проекта")
    industry = models.CharField('Вид деятельности', max_length=30)
    data_send = models.DateTimeField(default=timezone.now, blank=False, null = True)
    cost = models.CharField("Стоимость проекта", max_length=40)
    square = models.CharField("Площадь земельного участка", max_length=40)
    work = models.CharField("Колличество рабочих", max_length=5)
    company = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def send_statement(self):
        self.data_send = timezone.now()
        self.save()

    def __str__(self):
        return self.project_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, id=instance.id)
