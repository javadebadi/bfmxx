from django import forms

class AccountUploadFileForm(forms.Form):
    file = forms.FileField()