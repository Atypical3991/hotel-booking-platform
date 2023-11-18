from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from ..models.BaseModel import BaseModel


class HotelModel(BaseModel):
    class Category(models.TextChoices):
        BUSINESS = 'Business', 'Business'
        RESORT = 'Resort', 'Resort'
        BOUTIQUE = 'Boutique', 'Boutique'
        VACATION_HOME = 'VacationHome', 'Vacation Home'

    class Amenities(models.TextChoices):
        WIFI = 'W', 'Free Wi-Fi'
        PARKING = 'P', 'Parking'
        POOL = 'PL', 'Swimming Pool'
        GYM = 'G', 'Fitness Center'
        SPA = 'S', 'Spa'

    name = models.CharField(max_length=100,unique=True)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    amenities = ArrayField(models.CharField(max_length=100,choices=Amenities.choices,blank=True,null=True))
    images = ArrayField(models.URLField(max_length=1000, blank=True,null=True))
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    category = models.CharField(max_length=100, choices=Category.choices,blank=True, null=True)
    hotelier_id = models.IntegerField(null=False,blank=False)
    active = models.BooleanField(null=False,blank=False,default=True)