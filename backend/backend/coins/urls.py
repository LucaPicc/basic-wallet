from django.urls import path
from .views import CoinList, TransactionsView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('coin-list/', CoinList.as_view()),
    path('transactions/', TransactionsView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

