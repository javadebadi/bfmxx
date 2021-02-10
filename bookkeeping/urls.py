from django.urls import path, include

from .views import create_account
from .views import upload_accounts_csv
from .views import AccountListView

urlpatterns = [
    path('account/create/', create_account),
    path('account/create/upload', upload_accounts_csv),
    path('account/list/', AccountListView.as_view(template_name="bookkeeping/account/account_list.html") ),
]
