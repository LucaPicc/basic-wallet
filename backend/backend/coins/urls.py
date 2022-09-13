from django.urls import path
from .views import BlockedTransactionsView, CoinList, TransactionsView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('coin-list/', CoinList.as_view(), name='coin-list'),
    path('transactions/', TransactionsView.as_view(), name='transactions'),
    path('blocked/', BlockedTransactionsView.as_view(), name='blocked')
]

urlpatterns = format_suffix_patterns(urlpatterns)

