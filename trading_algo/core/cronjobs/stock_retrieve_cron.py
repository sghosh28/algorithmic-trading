# import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# import django
# django.setup()
from django.contrib.auth.models import User
from core.models import UserStrategyFilterMapModel, StocksToBuyModel
from core.utility import chartlink_utility, stock_positions_utility

def stock_retrieve_cron():
    """Cronjob to retrieve stock data from chartlink"""
    # Get all stock symbols
    # print("hello")
    users = User.objects.all()
    print(users)
    # write hello to a file named output.txt
    # with open('output.txt', 'w') as f:
    #     f.write("hello")
    #     f.write("hello")
    print("hello")
    user = users[0]
    print(user)

    mapp = UserStrategyFilterMapModel.objects.get(user=user)
    _filter = mapp._filter
    strategy = mapp.strategy
    print(_filter)
    stocks = chartlink_utility(_filter)
    to_buy = stock_positions_utility(stocks, strategy)
    print(to_buy)
    bulk_stocks = []
    for stock in to_buy:
        stock_to_buy = StocksToBuyModel()
        stock_to_buy.user = user
        stock_to_buy.stock_name = stock['name'] 
        stock_to_buy.stock_symbol = stock['nsecode']
        stock_to_buy.closing_amount = stock['close']
        stock_to_buy.entry_price = stock['entry_price']
        stock_to_buy.stop_loss = stock['stop_loss']
        stock_to_buy.target = stock['target']
        stock_to_buy.risk = stock['risk']
        stock_to_buy.position = stock['position']
        stock_to_buy.date_to_buy = stock['date_to_buy']
        bulk_stocks.append(stock_to_buy)
    StocksToBuyModel.objects.bulk_create(bulk_stocks)
    # write to_buy to a file named output.txt
    # with open('output.txt', 'w') as f:
    #     f.write(str(to_buy))

            # if qs is None:
            #     continue
            # strategy = qs.strategy
            # filter_strat = qs.filter
            # stocks_list = chartlink_utility(filter_strat)
            # print(stocks_list)
            # stock_positions = stock_positions_utility(stocks_list, strategy)
            # print(stock_positions)
    # Get stock data for each stock symbol
    # for stock_symbol in stock_symbols:
    #     stock_retrieve(stock_symbol.symbol)

    return True

# if __name__ == '__main__':
#     stock_retrieve_cron()