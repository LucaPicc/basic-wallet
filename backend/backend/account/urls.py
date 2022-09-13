from django.urls import path
from .views import AccountView, GetUsers
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('account/', AccountView.as_view(), name='account'),
    path('users/', GetUsers.as_view(), name='users')
]

urlpatterns = format_suffix_patterns(urlpatterns)

