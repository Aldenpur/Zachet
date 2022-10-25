import pandas as pandas
from django.db import models


class Securities(models.Model):
    title = models.CharField(max_length=255)
    code = models.IntegerField(unique=True, primary_key=True)
    type = models.CharField(max_length=255)
    platform = models.ForeignKey('Platforms', on_delete=models.PROTECT)

class Platforms(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=255, blank=True)


class TradingData(models.Model):
    date = models.DateField()
    price = models.IntegerField()
    secur_code = models.ForeignKey('Securities', on_delete=models.PROTECT)


# >>> from ZachetDB.models import TradingData
# SUM = 0
#>>> for q in TradingData.objects.filter(secur_code='1', date='2020-01-01'):
#...     SUM = SUM + q.price
#...     print(SUM)







