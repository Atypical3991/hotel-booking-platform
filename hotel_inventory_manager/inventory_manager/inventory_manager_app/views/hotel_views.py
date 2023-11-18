from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser

from ..models import HotelModel
from ..serializers.add_or_update_hotel import \
    AddOrUpdateHotelSerializer
from ..utils.ResonseHandler import CustomRESTResponseHandler


class HotelView:

    @staticmethod
    @api_view(['POST'])
    def add_hotel(request):
        # Parse the incoming JSON data
        data = JSONParser().parse(request)

        # Serialize the data
        serializer = AddOrUpdateHotelSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

        return CustomRESTResponseHandler(data=None, message="Customer created successfully", error=serializer.errors,
                                         status_m="failure", status=400)

    @staticmethod
    @api_view(['GET'])
    def get_hotel(request, hotel_id):
        pass

    @staticmethod
    @api_view(['POST'])
    def update_hotel(request, hotel_id):
        # fetch hotel instance
        hotel_instance = get_object_or_404(HotelModel, id=hotel_id)

        # Parse the incoming JSON data
        data = JSONParser().parse(request)

        # Serialize the data
        serializer = AddOrUpdateHotelSerializer(data=data, instance=hotel_instance)

        if serializer.is_valid():
            serializer.save()

        return CustomRESTResponseHandler(data=None, message="Customer created successfully", error=serializer.errors,
                                         status_m="failure", status=400)

    @staticmethod
    @api_view(['PUT'])
    def activate_hotel(request, hotel_id):
        # fetch hotel instance
        hotel_instance = get_object_or_404(HotelModel, id=hotel_id)

        # set active flag True
        hotel_instance.active = True

        # update hotel instance
        hotel_instance.save()

    @staticmethod
    @api_view(['PUT'])
    def deactivate_hotel(request, hotel_id):
        # fetch hotel instance
        hotel_instance = get_object_or_404(HotelModel, id=hotel_id)

        # set active flag True
        hotel_instance.active = False

        # update hotel instance
        hotel_instance.save()
