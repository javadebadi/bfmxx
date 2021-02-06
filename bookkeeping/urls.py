from django.urls import path, include

from .views import create_account

urlpatterns = [
    path('account/create/', create_account),
]
