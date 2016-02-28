from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=256)
    name_short = models.CharField(max_length=10)
    def __str__(self):
        return '{0} ({1})'.format(self.name, self.name_short)

class Room(models.Model):
    name = models.CharField(max_length=50)
    building = models.ForeignKey(Building, on_delete=models.PROTECT)
    row_top = models.IntegerField()
    row_bottom = models.IntegerField()
    label = models.BooleanField
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=256)
    number = models.CharField(max_length=5)
    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Colour(models.Model):
    name = models.CharField(max_length=50)
    hex_value = models.CharField(max_length=6)     # Hex RGB value
    def __str__(self):
        return '{0} ({1})'.format(self.name, self.hex_value)

class User(models.Model):
    name = models.CharField(max_length=50)
    colour = models.ForeignKey(Colour, on_delete=models.PROTECT)     # Hex RGB value
    def __str__(self):
        return self.name

class OrderType(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Note(models.Model):
    note = models.TextField()

class Setup(models.Model):
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    resource = models.ForeignKey(Resource, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    order_type = models.ForeignKey(OrderType, on_delete=models.PROTECT)
    setup_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='setups')
    setup_time = models.DateTimeField(null=True)
    pickup_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='pickups')
    pickup_time = models.DateTimeField(null=True)
    note = models.ForeignKey(Note, on_delete=models.SET_NULL, null=True)


