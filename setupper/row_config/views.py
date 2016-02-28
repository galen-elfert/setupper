from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader

# Create your views here.

def row_config(request, building):
    template = loader.get_template('row_config/row_config.html')
    context = {
        'building': building,
    }
    return HttpResponse(template.render(context, request))
