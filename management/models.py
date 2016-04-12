from django.db import models

class Valuta(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Название')
    abbreviation = models.CharField(max_length = 20, verbose_name = 'сокращение')

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюта'
    
class Tariff(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'название тариффа')
    valuta = models.ForeignKey(Valuta, verbose_name = 'валюта')
    units = models.IntegerField(verbose_name = 'Единицы')

    class Meta:
        verbose_name = 'Тарифф'
        verbose_name_plural = 'Тариффы'
    
class Room(models.Model):
    number = models.IntegerField(verbose_name = 'Номер комнаты')
    tariff = models.ForeignKey(Tarrif, verbose_name = 'Тарифф')
    is_free = models.BooleanField(verbose_name = 'Свободна/занята')

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

class Unit_of_measurement(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Полное название')
    reduction = models.CharField(max_length = 50, verbose_name = 'Сокращение')

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

class Additional_payment(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Название платежа')
    unit_of_measurement = models.ForeignKey(Unit_of_measurement, verbose_name = 'Единица измерения')
    tariff = models.ForeignKey(Tariff, verbose_name = 'Тарифф')
    bill = models.ForeignKey(Bill, verbonse_name = 'Итоговый счет', on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Дополнительный платеж'
        verbose_name_plural = 'Дополнительные платежи'
        
class Bill(models.Model):
    room = models.ForeignKey(Room, verbose_name = 'Комната')
    date = models.DateField(varbose_name = 'Дата платежа')
    total = models.DecimalField(verbose_name = 'Итог')

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'

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
    bill = models.ForeignKey(Bill, on_delete = models.CASCADE, verbose_name = 'счет')

    class Meta:
        verbose_name = 'Запись о регистрации'
        verbose_name_plural = 'Записи о регистрации'




    
