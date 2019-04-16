from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def shopper(request):
    return HttpResponse('<h1>Index Page</h1>')