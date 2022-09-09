# Generated by Django 4.1 on 2022-09-09 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

def create_basic_coins(apps, schema_editor):
    basic_coins = [
        {
            'name': 'United State Dolar',
            'short_name': 'USD',
            'is_reference': True,
            'category': 'fiat',
            'value_vs_reference': 1.0000
        },
        {
            'name': 'Peso Argentino',
            'short_name': 'ARS',
            'is_reference': False,
            'category': 'fiat',
            'value_vs_reference': 300.0000
        }
    ]
    Coins = apps.get_model('coins', 'Coin')

    for coin in basic_coins:
        Coins.objects.create(**coin)
    


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('regular', 'regular'), ('blocked', 'blocked')], default='regular', max_length=20)),
                ('balance', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('short_name', models.CharField(max_length=5)),
                ('category', models.CharField(choices=[('fiat', 'fiat'), ('cripto', 'cripto')], default='fiat', max_length=100)),
                ('is_reference', models.BooleanField(default=False)),
                ('value_vs_reference', models.DecimalField(decimal_places=4, default=1.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balances', models.ManyToManyField(to='coins.balance')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(choices=[('send', 'send'), ('reception', 'reception'), ('deposit', 'deposit'), ('withdrawal', 'withdrawal')], db_index=True, default='send', max_length=10)),
                ('code', models.CharField(blank=True, db_index=True, default='', max_length=255)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('valid', models.BooleanField(default=False)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coins.coin')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('transmitter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transimitter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='balance',
            name='coin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coins.coin'),
        ),
        migrations.AddField(
            model_name='balance',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='balance',
            name='transaction',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='coins.transactions'),
        ),
        migrations.RunPython(create_basic_coins)
    ]
