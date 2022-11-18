# Generated by Django 4.1.2 on 2022-10-21 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('scan_clause', models.CharField(max_length=200)),
                ('post_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StrategyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('entry_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stop_loss_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('target_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('position', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='StocksToBuyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100)),
                ('stock_symbol', models.CharField(max_length=100)),
                ('closing_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('entry_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stop_loss', models.DecimalField(decimal_places=2, max_digits=10)),
                ('target', models.DecimalField(decimal_places=2, max_digits=10)),
                ('risk', models.DecimalField(decimal_places=2, max_digits=10)),
                ('position', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_generated', models.DateTimeField(auto_now_add=True)),
                ('date_to_buy', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
