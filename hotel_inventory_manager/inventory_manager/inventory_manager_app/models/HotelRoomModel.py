from django.db import models

from ..models.BaseModel import BaseModel
from ..models.HotelModel import HotelModel


class HotelRoomModel(BaseModel):
    class Category(models.TextChoices):
        STANDARD = 'Standard', 'Standard Room'
        DELUXE = 'Deluxe', 'Deluxe Room'
        SUITE = 'Suite', 'Suite'

    class BedCategory(models.TextChoices):
        SINGLE = 'Single', 'Single Bed'
        DOUBLE = 'Double', 'Double Bed'
        KING = 'King', 'King Size Bed'

    class BreakfastCategories(models.TextChoices):
        AVAILABLE = 'Available', 'Available'
        NOT_AVAILABLE = 'Not Available', 'Not Available'

    class DinnerCategories(models.TextChoices):
        AVAILABLE = 'Available', 'Available'
        NOT_AVAILABLE = 'Not Available', 'Not Available'

    class PaxCategory(models.TextChoices):
        SINGLE = 'Single', 'Single Pax'
        DOUBLE = 'Double', 'Double Pax'
        FAMILY = 'Family', 'Family Pax'
        SUITE = 'Suite', 'Suite Pax'

    class ViewCategory(models.TextChoices):
        CITY = 'City', 'City View'
        OCEAN = 'Ocean', 'Ocean View'
        MOUNTAIN = 'Mountain', 'Mountain View'
        GARDEN = 'Garden', 'Garden View'
        POOL = 'Pool', 'Pool View'
        COURTYARD = 'Courtyard', 'Courtyard View'
        PARK = 'Park', 'Park View'

    hotel = models.ForeignKey(HotelModel, on_delete=models.CASCADE)
    type = models.CharField(choices=Category.choices, max_length=100, null=False, blank=False)
    bed = models.CharField(choices=BedCategory.choices, max_length=100, null=False, blank=False)
    breakfast = models.CharField(choices=BreakfastCategories.choices, max_length=100, null=False, blank=False)
    dinner = models.CharField(choices=DinnerCategories.choices, max_length=100, null=False, blank=False)
    checkin_time = models.DateTimeField(null=False, blank=False)
    checkout_time = models.DateTimeField(null=False, blank=False)
    pax = models.CharField(choices=PaxCategory.choices, max_length=100, null=False, blank=False)
    view = models.CharField(choices=ViewCategory.choices, max_length=100)
    active = models.BooleanField(default=True)
