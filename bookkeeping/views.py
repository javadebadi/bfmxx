import csv
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from bookkeeping.models import Account
from .forms import AccountUploadFileForm
from .forms import AccountCreateForm

# Create your views here.
def account_create(request):
    """The functions creates an account by handling the request
    """
    if request.method == 'GET':
        form = AccountCreateForm()
        context={"form":form}
        return render(request, 'bookkeeping/account/account_create.html',context=context)
    if request.method == 'POST':
        form = AccountCreateForm(request.POST)
        if form.is_valid():
            account = Account()
            account.account_name = form.cleaned_data['account_name']
            account.account_type = form.cleaned_data['account_type']
            account.account_category = form.cleaned_data['account_category']
            account.account_description = form.cleaned_data['account_description']
            account.save()
            form = AccountCreateForm()
        return HttpResponseRedirect('../list')
    

# a list view of accounts
class AccountListView(ListView):
    model = Account
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# a view to upload accounts
def upload_accounts_csv(request):
    account = Account()
    if request.method == 'POST':
        form = AccountUploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_in_memory = request.FILES['file']
            account.fill_from_csv(file_in_memory=file_in_memory)
            return HttpResponseRedirect('../list')
    else:
        form = AccountUploadFileForm()
    return render(request, 'bookkeeping/account/account_upload.html', {'form': form})