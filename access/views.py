from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def sign_up(request):
    return render(request, 'sign_up.html', {
        'form': UserCreationForm
    })
