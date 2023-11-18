from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser

from ..models.HotelModel import HotelModel
from ..models.HotelRoomModel import HotelRoomModel
from ..serializers.add_or_update_hotel_room import AddOrUpdateHotelRoomSerializer
from ..utils.ResonseHandler import CustomRESTResponseHandler


class HotelRoomView:

    @staticmethod
    @api_view(['POST'])
    def add_hotel_room(request, hotel_id):
        # fetch hotel instance
        hotel_instance = get_object_or_404(HotelModel, id=hotel_id)

        # Parse the incoming JSON data
        data = JSONParser().parse(request)

        # Serialize the data
        serializer = AddOrUpdateHotelRoomSerializer(data=data)

        if serializer.is_valid():
            hotel_room_instance = serializer.save()
            hotel_room_instance.hotel = hotel_instance
            hotel_room_instance.save()

        return CustomRESTResponseHandler(data=None, message="Hotel room created successfully", error=serializer.errors,
                                         status_m="failure", status=400)

    @staticmethod
    @api_view(['GET'])
    def get_hotel_room(request, room_id):
        hotel_room_instance = get_object_or_404(HotelRoomModel, id=room_id)
        pass

    @staticmethod
    @api_view(['POST'])
    def update_hotel_room(request, room_id):
        hotel_room_instance = get_object_or_404(HotelRoomModel, id=room_id)

        # Parse the incoming JSON data
        data = JSONParser().parse(request)

        # Serialize the data
        serializer = AddOrUpdateHotelRoomSerializer(data=data, instance=hotel_room_instance)

        if serializer.is_valid():
            serializer.save()

        return CustomRESTResponseHandler(data=None, message="Hotel room updated successfully", error=serializer.errors,
                                         status_m="failure", status=400)

    @staticmethod
    @api_view(['PUT'])
    def activate_hotel_room(request, hotel_room_id):
        pass

    @staticmethod
    @api_view(['PUT'])
    def deactivate_hotel_room(request, hotel_room_id):
        pass
