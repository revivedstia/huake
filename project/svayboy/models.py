from django.db import models


class Calls(models.Model):
    name = models.CharField('Имя', max_length=50)
    phone_number = models.IntegerField('Телефон')
    email = models.EmailField('Почта', max_length=50)
    message = models.CharField('Сообщение', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка на звонок'
        verbose_name_plural = 'Заявки на звонки'


class Svayboy(models.Model):
    title = models.CharField('Название', max_length=50)
    ru_title = models.CharField('Название на русском', max_length=50, default='Сваебойная машина ')

    state = models.CharField('Состояние', max_length=50, default='под заказ')
    prise = models.IntegerField('Цена', default=0)

    engine = models.CharField('Двигатель', max_length=50, default='500', blank=True, null=True)
    do_wya = models.CharField('Способ езды', max_length=50, default='Ручная механическая коробка', blank=True,
                                    null=True)
    wheels = models.CharField('Колесная база', max_length=50, default='', blank=True, null=True)
    v = models.CharField('Скорость движения', max_length=50, default='', blank=True, null=True)
    p = models.CharField('Давление гидравлического насоса', max_length=50, default='', blank=True, null=True)
    power = models.CharField('Мощность', max_length=50, default='42 кВт', blank=True, null=True)
    fuel = models.CharField('Расход топлива', max_length=50, default='42 кВт', blank=True, null=True)

    mass = models.CharField('Масса', max_length=50, default='3 тонны', blank=True, null=True)
    dimension = models.CharField('Габариты', max_length=50, default='', blank=True, null=True)

    image1 = models.ImageField(upload_to='imag/')
    image2 = models.ImageField(upload_to='imag/', blank=True, null=True)
    image3 = models.ImageField(upload_to='imag/', blank=True, null=True)
    image4 = models.ImageField(upload_to='imag/', blank=True, null=True)
    image5 = models.ImageField(upload_to='imag/', blank=True, null=True)

    def __str__(self):
        return self.ru_title

    class Meta:
        verbose_name = 'Своебойная машина'
        verbose_name_plural = 'Своебойные машины'
