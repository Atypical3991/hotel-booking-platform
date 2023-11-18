from django.db import models

from .BaseModel import BaseModel


class Customer(BaseModel):
    username = models.CharField(max_length=100, db_index=True, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=32, blank=False, null=False)
    address = models.CharField(max_length=256, blank=False, null=False)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20, unique=True, blank=False, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"
