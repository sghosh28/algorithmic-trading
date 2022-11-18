from django.urls import path


from . import views

urlpatterns = [
    path('', views.UserLogInView.as_view(), name='index'),
]