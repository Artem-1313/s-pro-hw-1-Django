from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def get_date(request):
    return HttpResponse(datetime.today().strftime('%d.%m.%Y'))

def get_year(request):
    return HttpResponse(datetime.now().year)

def get_day(request):
    return HttpResponse(datetime.now().day)

def get_month(request):
    return HttpResponse(datetime.now().month)