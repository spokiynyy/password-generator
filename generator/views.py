from typing import Generator
from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'Generator/home.html')

def credit(request):
    return render(request,'Generator/credit.html')

def password(request):

    characters = list('abcdefghijklmopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('123456789'))

    length =  int(request.GET.get('length', 12))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^^&*()'))

    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'Generator/password.html', {'password': thepassword})

# Create your views here.
