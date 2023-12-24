from django.http import HttpResponse
from ...forms import MyForm
from django.shortcuts import render
from .handlers import transformTextHandler

# take a request from the user with a text field and transform it to uppercase and return it to the user.
def transform(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            text = transformTextHandler(form.cleaned_data)
            return HttpResponse(text)
        else:
            return HttpResponse("Invalid form")
    else:
        return HttpResponse(request.method + " is not supported")