from django.db import models

class Valuta(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Название')
    abbreviation = models.CharField(max_length = 20, verbose_name = 'Сокращение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюта'
    
class Tariff(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Название тариффа')
    valuta = models.ForeignKey(Valuta, verbose_name = 'Валюта')
    units = models.IntegerField(verbose_name = 'Единицы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'
    
class Room(models.Model):
    number = models.IntegerField(verbose_name = 'Номер комнаты')
    tariff = models.ForeignKey(Tariff, verbose_name = 'Тариф')
 
    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return str(self.number)

class Unit_of_measurement(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Полное название')
    reduction = models.CharField(max_length = 50, verbose_name = 'Сокращение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

class Record(models.Model):
    first_name = models.CharField(max_length = 50, verbose_name = 'Имя')
    middle_name = models.CharField(max_length = 50, verbose_name = 'Отчество')
    last_name = models.CharField(max_length = 50, verbose_name = 'Фамилия')
    country = models.CharField(max_length = 50, verbose_name = 'Страна')
    city = models.CharField(max_length = 50, verbose_name = 'Город')
    passport_series = models.IntegerField(verbose_name = 'Серия паспорта')
    passport_id = models.IntegerField(verbose_name = 'Номер паспорта')
    issued = models.CharField(max_length = 200, verbose_name = 'Кем выдан')
    date_of_birth = models.DateField(verbose_name = 'Дата рождения')
    date_in = models.DateField(verbose_name = 'Дата въезда')
    date_out = models.DateField(verbose_name = 'Дата выезда')
    total = models.DecimalField(max_digits = 19, decimal_places = 2,verbose_name = 'Итог')
    room = models.ForeignKey(Room, verbose_name = 'Комната')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Запись о регистрации'
        verbose_name_plural = 'Записи о регистрации'

class Service(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Сервис')
    price = models.DecimalField(max_digits = 19, decimal_places = 2,verbose_name = 'Стоимость')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

class Additional_payment(models.Model):
    unit_of_measurement = models.ForeignKey(Unit_of_measurement, verbose_name = 'Единица измерения')
    size = models.IntegerField(verbose_name = 'Количество')
    service = models.ForeignKey(Service, verbose_name = 'Сервис')
    record = models.ForeignKey(Record)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дополнительный платёж'
        verbose_name_plural = 'Дополнительные платежи'

    
