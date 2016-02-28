from django.contrib import admin

from .models import Setup
from .models import Colour
from .models import Building
from .models import Room

# Register your models here.
admin.site.register(Setup)
admin.site.register(Colour)
admin.site.register(Building)
admin.site.register(Room)
