import pytz
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person", null=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30, blank=True)
    birth_date = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=2)
    job = models.CharField(max_length=30)
    added_date = models.DateTimeField(default=timezone.now())
    added_by = models.CharField(max_length=30)

    def __str__(self):
        return self.fname