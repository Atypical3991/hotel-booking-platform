from rest_framework import serializers

from ..models import HotelModel


class HotelDetails(serializers.Serializer):
    class Meta:
        model = HotelModel
        fields = 'name,address,pincode,city,state,amenities,images,rating,category'
