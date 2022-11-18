from turtle import position
from django.db import models


class StrategyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    entry_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    stop_loss_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    target_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    position = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name