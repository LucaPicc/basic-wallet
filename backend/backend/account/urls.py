from django.urls import path
from .views import AccountView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('account/', AccountView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

