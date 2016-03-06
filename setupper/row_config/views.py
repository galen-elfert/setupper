from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.core import serializers

from event_cal.models import Room, Building

# Create your views here.

def row_config(request, building):
    this_building = Building.objects.get(name_short=building)
    # room_list = Room.objects.filter(building=this_building)
    room_list = serializers.serialize('json', Room.objects.filter(building=this_building))
    template = loader.get_template('row_config/row_config.html')
    context = {
        'building': building,
        'room_list': room_list
    }
    return HttpResponse(template.render(context, request))
