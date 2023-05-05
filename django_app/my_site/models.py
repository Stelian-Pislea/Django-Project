from django.db import models
from datetime import datetime


# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.CharField(max_length=250)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=250)
    room = models.CharField(max_length=250)


    def __str__(self):
        return f'{self.user} -> {self.value[:15]} ...'
