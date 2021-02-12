from django.urls import path, include

from .views import account_create
from .views import upload_accounts_csv
from .views import AccountListView

urlpatterns = [
    path('account/create/', account_create, name='account_create'),
    path('account/create/upload', upload_accounts_csv, name='account_upload'),
    path('account/list/', AccountListView.as_view(template_name="bookkeeping/account/account_list.html") , name='account_list'),
]
