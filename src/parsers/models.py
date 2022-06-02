from django.db import models


class Money(models.Model):
    """Модель вида валюты"""
    name = models.CharField(max_length=255, unique=True)


class Quotation(models.Model):
    money = models.ForeignKey(to=Money, on_delete=models.CASCADE)
    date = models.DateTimeField()
    close_value = models.FloatField(verbose_name="Закрытие котировки", null=True, blank=True)
    open_value = models.FloatField(verbose_name="Открытие котировки", null=True, blank=True)
    high_value = models.FloatField(verbose_name="Наивысшее значение", null=True, blank=True)
    low_value = models.FloatField(verbose_name="Наименьшее значение", null=True, blank=True)
