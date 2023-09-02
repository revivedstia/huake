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


class Beton(models.Model):
    title = models.CharField('Название', max_length=50)
    ru_title = models.CharField('Название на русском', max_length=50, default='Бетоносмеситель')

    state = models.CharField('Состояние', max_length=50, default='под заказ')
    prise = models.IntegerField('Цена', default=0)

    engine = models.CharField('Двигатель', max_length=50, default='500', blank=True, null=True)
    transmission = models.CharField('Коробка передач', max_length=50, default='Ручная механическая коробка', blank=True, null=True)
    mixer = models.CharField('Объем смесиьеля', max_length=50, blank=True, null=True)

    direction = models.CharField('Формальное направление', max_length=50, default='', blank=True, null=True)
    stop = models.CharField('Тормозная система', max_length=50, default='', blank=True, null=True)
    water_supply = models.CharField('Способ подачи воды', max_length=50, default='', blank=True, null=True)
    lifting = models.CharField('Подъемная способность', max_length=50, default='', blank=True, null=True)
    tire = models.CharField('Размер шин', max_length=50, default='', blank=True, null=True)
    dimension = models.CharField('Габариты', max_length=50, default='', blank=True, null=True)

    image1 = models.ImageField(upload_to='imag/')
    image2 = models.ImageField(upload_to='imag/', blank=True, null=True)
    image3 = models.ImageField(upload_to='imag/', blank=True, null=True)
    image4 = models.ImageField(upload_to='imag/', blank=True, null=True)
    image5 = models.ImageField(upload_to='imag/', blank=True, null=True)

    def __str__(self):
        return self.ru_title

    class Meta:
        verbose_name = 'Бетоносмеситель'
        verbose_name_plural = 'Бетоносмесители'
