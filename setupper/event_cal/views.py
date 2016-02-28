from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader


# Create your views here.

def event_cal(request, building, year, month, day):
    template = loader.get_template('event_cal/index.html')
    context = {
        'building': building,
        'year': year,
        'month': month,
        'day': day,
    }
    return HttpResponse(template.render(context, request))


def upload(request):
    return HttpResponse("This will be the upload page")
