import csv
import re
from event_cal.models import Room
from event_cal.models import Building

rooms = []
pattern = r'[0-9][0-9-/]+[0-9]$'

def get_buildings_setup():
    pass

with open('temp_cal_data/20162601-events.csv') as csvfile:
    if re.search('events', csvfile.name):
        room_col = 19
        building = 'Harbour Centre'
    elif re.search('setup', csvfile.name):
        room_col = 16
        building_col = 0
        building = None
    
    reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    for row in reader:
        match = re.search(pattern, row[room_col])
        if building == None:
            building = row[building_col]
        if match:
            room = match.group(0)
        else:
            room = row[room_col]
        if room not in rooms:
            rooms.append(room)

building_object, created = Building.objects.get_or_create(name=building, defaults={'name_short':'Abbrev'})

for r in rooms:
    robj, c = Room.objects.get_or_create(name=r, building=building_object, defaults={'row_top':0, 'row_bottom':0})
    if c:
        print robj
