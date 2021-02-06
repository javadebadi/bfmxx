from django.shortcuts import render

# Create your views here.
def create_account(request):
    """The functions creates an account by handling the request
    """
    context={"Hello":"Hellow"}
    return render(request, 'bookkeeping/account/create.html',context=context)
