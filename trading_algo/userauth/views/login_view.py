from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from userauth.forms.login_form import LoginForm
from core.models import UserStrategyFilterMapModel
from core.utility import chartlink_utility, stock_positions_utility
class UserLogInView(View):
    
    def get(self, request):
        form = LoginForm() 
        return render(request, 'userauth/user_auth_base.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                mapp = UserStrategyFilterMapModel.objects.get(user=user)
                _filter = mapp._filter
                strategy = mapp.strategy
                print(_filter)
                stocks = chartlink_utility(_filter)
                to_buy = stock_positions_utility(stocks, strategy)
                # stocks = 'ok'
                return render(request, 'userauth/user_auth_base.html', {'form': form, 'stocks':stocks,'success': 'Logged in successfully'})
            else:
                return render(request, 'userauth/user_auth_base.html', {'form': form, 'error': 'Invalid credentials'})
        return render(request, 'userauth/user_auth_base.html', {'form': form})


def kuch():
    print('kuch')
    return True