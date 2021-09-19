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

"""
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
"""
# Create your models here.
