from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader


# Create your views here.

def event_cal(request, building, year, month, day):
    return HttpResponse("{0}, {1}-{2}-{3}".format(building, year, month, day))

def upload(request):
    return HttpResponse("This will be the upload page")
