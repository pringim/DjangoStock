from django.db import models
from django.db.models import Model


class StockMarket(Model):
    objects = None
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker
