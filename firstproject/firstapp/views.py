from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
# Create your views here.


def hellodjango(request):
    return HttpResponse("Hello, Django!")

def get_name(request, name):
    if name=="date":
        return HttpResponseRedirect("dateapp.get_date")
    return HttpResponse(f"Hello, {name}")

