from turtle import position
from django.db import models
from django.contrib.auth.models import User

class StocksToBuyModel(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=100)
    stock_symbol = models.CharField(max_length=100)
    closing_amount = models.DecimalField(max_digits=10, decimal_places=2)
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    stop_loss = models.DecimalField(max_digits=10, decimal_places=2)
    target = models.DecimalField(max_digits=10, decimal_places=2)
    risk = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.DecimalField(max_digits=10, decimal_places=2)
    date_generated = models.DateTimeField(auto_now_add=True)
    date_to_buy = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stock_symbol + " " + str(self.entry_price) + " " + str(self.date_to_buy)