from django.db import models
from django.contrib.auth.models import User
from .filter_model import FilterModel
from .strategy_model import StrategyModel


class UserStrategyFilterMapModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    strategy = models.ForeignKey(StrategyModel, on_delete=models.CASCADE)
    _filter = models.ForeignKey(FilterModel, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username + " " + self.strategy.name + " " + self._filter.name