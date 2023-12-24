from django.http import HttpResponse
from .forms import MyForm
from django.shortcuts import render


def index(request):
    form = MyForm()
    return render(request, 'form.html', {'form': form})