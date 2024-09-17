from django.db import models
from django.core.validators import MinValueValidator

from .constant import MEASURE_CHOICES


class Buyer(models.Model):
    """Модель для подотчетных лиц."""

    full_name= models.CharField('ФИО',
                                max_length=200)
    
    class Meta:
        verbose_name = 'Материально-ответственное лицо'
        verbose_name_plural = 'Материально-ответственные лица'
        ordering = ('full_name', )

    def __str__(self):
        return self.full_name
    

class Objects(models.Model):
    """Модель для объектов."""

    name = models.CharField("Наименование объекта",
                            max_length=250,
                            help_text='Укажите название объекта')
    
    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты строительства'
        ordering = ('name', )

    def __str__(self):
        return self.name


class Item(models.Model):
    """Модель для ТМЦ."""

    name = models.CharField('Наименование',
                            max_length=250,
                            )
    measurement_unit = models.CharField('Единица измерения',
        max_length=12,
        choices=MEASURE_CHOICES,
        help_text='Укажите единицу измерения',)
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        default=0,
        validators=(MinValueValidator(1,
                    message='Введите количество больше 0.'),))    
    buyer = models.ForeignKey(Buyer,
                              on_delete=models.PROTECT,
                            help_text='Выберите МОЛ')
    aim = models.ForeignKey(Objects,
                            on_delete=models.PROTECT,
                            help_text='Выберите объект')
    image = models.ImageField('Картинка',)
    note = models.TextField("Комментарий")

    class Meta:
        verbose_name = 'ТМЦ'
        verbose_name_plural = 'ТМЦ'
        ordering = ('name', )

    def __str__(self):
        return f'{self.name}: {self.amount} {self.measurement_unit}'
