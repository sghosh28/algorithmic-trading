from decimal import Decimal
from turtle import position
from datetime import timedelta, datetime
# from django.utils.timezone import datetime
from decimal import Decimal

def stock_positions_utility(stocks_list, strategy):
    """This function is used to get the stock positions for each stock"""
    entry = strategy.entry_percentage/100
    stop_loss_percentage = strategy.stop_loss_percentage/100
    target_percentage = strategy.target_percentage/100
    position = strategy.position

    for stock in stocks_list:
        stock['close'] = round(Decimal(stock['close']),3)
        stock['entry_price'] = round(stock['close'] + (stock['close'] * entry),3)
        stock['stop_loss'] = round(stock['entry_price'] + (stock['entry_price'] * stop_loss_percentage),3)
        stock['target'] = round(stock['entry_price'] - (stock['entry_price'] * target_percentage),3)
        stock['risk'] = round(stock['stop_loss'] - stock['entry_price'],3)
        stock['position'] = round(position/stock['risk'],3)
        stock['date_generated'] = datetime.now()
        # stock['date_to_buy'] = stock['date_generated'] + timedelta(days=1)
        # date to buy is 1 day after date generated
        stock['date_to_buy'] = stock['date_generated'] + timedelta(days=1)
    return stocks_list