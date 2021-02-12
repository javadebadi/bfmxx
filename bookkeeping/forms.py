from django import forms
from django.forms import ModelForm
from .models import Account

class AccountUploadFileForm(forms.Form):
    file = forms.FileField()

class AccountCreateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["account_name", "account_type", "account_category", "account_description"]
        widgets = {
            "account_description": forms.Textarea,
            "account_name": forms.TextInput,
            "account_type": forms.RadioSelect,
        }
