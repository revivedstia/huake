from django.db import models


class CallsModel(models.Model):
    name = models.CharField('Имя', max_length=50)
    phone_number = models.IntegerField('Телефон')
    email = models.EmailField('Почта', max_length=50)
    message = models.CharField('Сообщениеttt', max_length=250)
    time = models.DateTimeField('Время отправки  (UTC 0)', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка на звонок'
        verbose_name_plural = 'Заявки на звонки'
