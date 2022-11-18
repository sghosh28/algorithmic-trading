from django.contrib import admin
from .models import StocksToBuyModel, StrategyModel, UserStrategyFilterMapModel, FilterModel

# Register your models here.

admin.site.register(StocksToBuyModel)
admin.site.register(StrategyModel)
admin.site.register(UserStrategyFilterMapModel)
admin.site.register(FilterModel)