from rest_framework import serializers


class GetCustomerProfileByIdSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=30, required=True)
    email = serializers.EmailField(max_length=100, required=True);
    mobile_number = serializers.CharField(max_length=20, required=True)


class GetHotelierProfileByIdSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=30, required=True)
    email = serializers.EmailField(max_length=100, required=True);
    mobile_number = serializers.CharField(max_length=20, required=True)
