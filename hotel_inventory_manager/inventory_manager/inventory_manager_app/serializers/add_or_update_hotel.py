import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models.HotelModel import HotelModel


class AddOrUpdateHotelSerializer(serializers.Serializer):

    def validate_name(self, value):
        # Define your pattern using a regular expression
        # username should contain only aphabets,numbers and underscores
        pattern = re.compile(r'^[a-zA-Z0-9.]*$')

        # Check if the value matches the pattern
        if not pattern.match(value):
            raise ValidationError('Invalid format. Only letters, numbers and underscores are allowed.')

        return value

    def validate_pincode(self, value):
        # Define your pattern using a regular expression
        # Regex pattern for validating indian pincode numbers, should start with any digit from 1 to 9 and
        # total of 6 digits
        pattern = re.compile(r'^[1-9][0-9]{5}$')

        # Check if the value matches the pattern
        if not pattern.match(value):
            raise ValidationError('Invalid format.Pincode should start with any digit from 1 to 9 with '
                                  'total of 6 digits.')

        return value

    def validate_state(self, value):
        # Define your pattern using a regular expression
        # only alphabets are allowed
        pattern = re.compile(r'^[a-zA-Z]*$')

        # Check if the value matches the pattern
        if not pattern.match(value):
            raise ValidationError('Invalid format. Only letters are allowed.')

        return value

    def validate_city(self, value):
        # Define your pattern using a regular expression
        # only alphabets are allowed
        pattern = re.compile(r'^[a-zA-Z]*$')

        # Check if the value matches the pattern
        if not pattern.match(value):
            raise ValidationError('Invalid format. Only letters are allowed.')

        return value

    class Meta:
        model = HotelModel
        fields = 'name,address,pincode,city,state,amenities,images,rating,category'


