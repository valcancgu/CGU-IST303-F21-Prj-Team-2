from django.db import models
from datetime import datetime
import uuid


class DBService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_name = models.CharField(max_length=128)
    cost_per_minute = models.FloatField()
    duration = models.IntegerField()

    def __repr__(self):
        return f"{self.service_name}: {self.duration} mins – {self.cost_per_minute} per minute"

    def __str__(self):
        return f"{self.service_name}: {self.duration} mins – {self.cost_per_minute} per minute"


class DBGuest(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=32)


class DBAppointment(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    service = models.CharField(max_length=32)
    guest = models.IntegerField()
    date = models.DateField()
    start_time = models.TimeField()

    class Meta:
        ordering = ['-date', '-start_time']
