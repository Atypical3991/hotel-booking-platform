import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models.HotelModel import HotelModel


class AddOrUpdateHotelRoomSerializer(serializers.Serializer):
    hotel_id = serializers.IntegerField()

    class Meta:
        model = HotelModel
        fields = 'type,bed,breakfast,dinner,checkin_time,checkout_time,pax,view,'


