from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.


class Records(models.Model):
    city = models.CharField('Город', max_length=100)
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    windspeed = models.FloatField()
    history = HistoricalRecords()

    def __str__(self):
        return self.city

    def get_absolute_url(self):
        return '/data/'

    class Meta:
        verbose_name = 'Погода'
        verbose_name_plural = 'Погода'


class Cities(models.Model):
    city = models.CharField('Город', max_length=100)
    city_coords = models.CharField(max_length=50)
    # history = HistoricalRecords()

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Equipment_spots(models.Model):
    equipment = models.CharField('Оборудование', max_length=100)
    nearest_city = models.CharField('Город', max_length=100)
    # history = HistoricalRecords()

    def __str__(self):
        return self.equipment

    class Meta:
        verbose_name = 'Станция с оборудованием'
        verbose_name_plural = 'Станции с оборудованием'


class Equipment_models(models.Model):
    equipment_type = models.CharField('Тип оборудования', max_length=20)
    equipment_model = models.CharField('Модель оборудования', max_length=100)
    equipment_cost = models.FloatField()
    # history = HistoricalRecords()

    def __str__(self):
        return self.equipment_type

    class Meta:
        verbose_name = 'Модель оборудования'
        verbose_name_plural = 'Модели оборудования'


class Month_avg(models.Model):
    city = models.CharField('Город', max_length=100)
    month = models.CharField('Месяц', max_length=25)
    year = models.IntegerField()
    temperature_avg = models.FloatField()
    humidity_avg = models.FloatField()
    windspeed_avg = models.FloatField()
    # history = HistoricalRecords()

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Среднее значение за месяц'
        verbose_name_plural = 'Средние значения за месяцы'


class Year_avg(models.Model):
    city = models.CharField('Город', max_length=100)
    year = models.IntegerField()
    temperature_avg = models.FloatField()
    humidity_avg = models.FloatField()
    windspeed_avg = models.FloatField()
    # history = HistoricalRecords()

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Среднее значение за год'
        verbose_name_plural = 'Средние значения за годы'
