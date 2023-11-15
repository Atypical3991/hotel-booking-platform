import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models.CustomerModel import Customer


class CreateCustomerSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=30, required=True)
    email = serializers.EmailField(max_length=100, required=True);
    password = serializers.CharField(max_length=32, required=True)
    address = serializers.CharField(max_length=256, required=True)
    city = serializers.CharField(max_length=100, required=False)
    state = serializers.CharField(max_length=200, required=False)
    pincode = serializers.CharField(max_length=20, required=False)
    mobile_number = serializers.CharField(max_length=20, required=True)

    def create(self, validated_data):
        Customer.objects.create(**validated_data)

    def validate_username(self, value):
        # Define your pattern using a regular expression
        # username should contain only aphabets,numbers and underscores
        pattern = re.compile(r'^[a-zA-Z0-9_]*$')

        # Check if the value matches the pattern
        if not pattern.match(value):
            raise ValidationError('Invalid format. Only letters, numbers and underscores are allowed.')

        return value

    def validate_first_name(self, value):
        # Define your pattern using a regular expression
        # only alphabets are allowed
        pattern = re.compile(r'^[a-zA-Z]*$')

        # Check if the value matches the pattern
        if not pattern.match(value):
            raise ValidationError('Invalid format. Only letters are allowed.')

        return value

    def validate_last_name(self, value):
        # Define your pattern using a regular expression
        # only alphabets are allowed
        pattern = re.compile(r'^[a-zA-Z]*$')

        # Check if the value matches the pattern
        if not pattern.match(value):
            raise ValidationError('Invalid format. Only letters are allowed.')

        return value

    def validate_password(self, value):
        # Define your pattern using a regular expression
        # password should contain, at least one alphabet, at least one digit,  one special char and
        # minimum of 8 chars length
        pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

        # Check if the value matches the pattern
        if not pattern.match(value):
            raise ValidationError('Invalid format. Password should contain at least one alphabet, one digit, '
                                  'one special character and minimum length of 8 characters')

        return value

    def validate_mobile_number(self, value):
        # Define your pattern using a regular expression
        # Regex pattern for validating indian mobile numbers, starting with 7,8 or 9 and total of 10 digits
        pattern = re.compile(r'^[789]\d{9}$')

        # Check if the value matches the pattern
        if not pattern.match(value):
            raise ValidationError('Invalid format. Mobile number should start with 7,8 or 9 with total of 10 digits.')

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


class UpdateCustomerSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100, required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    password = serializers.CharField(max_length=100, required=False)
    address = serializers.CharField(max_length=100, required=False)
    city = serializers.CharField(max_length=50, required=False)
    state = serializers.CharField(max_length=50, required=False)
    pincode = serializers.CharField(max_length=20, required=False)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get("password", instance.password)
        instance.address = validated_data.get("address", instance.password)
        instance.city = validated_data.get("city", instance.city)
        instance.state = validated_data.get("status", instance.state)
        instance.pincode = validated_data.get("pincode", instance.pincode)
        instance.save()
        return instance

    def validate_first_name(self, value):
        # Define your pattern using a regular expression
        # only alphabets are allowed
        pattern = re.compile(r'^[a-zA-Z]*$')

        # Check if the value matches the pattern
        if not pattern.match(value):
            raise ValidationError('Invalid format. Only letters are allowed.')

        return value

    def validate_last_name(self, value):
        # Define your pattern using a regular expression
        # only alphabets are allowed
        pattern = re.compile(r'^[a-zA-Z]*$')

        # Check if the value matches the pattern
        if not pattern.match(value):
            raise ValidationError('Invalid format. Only letters are allowed.')

        return value

    def validate_password(self, value):
        # Define your pattern using a regular expression
        # password should contain, at least one alphabet, at least one digit,  one special char and
        # minimum of 8 chars length
        pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

        # Check if the value matches the pattern
        if not pattern.match(value):
            raise ValidationError('Invalid format. Password should contain at least one alphabet, one digit, '
                                  'one special character and minimum length of 8 characters')

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


class CustomerLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)


class CustomerLogoutSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    role = serializers.CharField(max_length=20, required=True)
