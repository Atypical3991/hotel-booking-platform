from django.db import models

from .BaseModel import BaseModel


class Hotelier(BaseModel):
    username = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20, unique=True)
    active = models.BooleanField
    business_name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"
