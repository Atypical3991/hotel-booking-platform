from django.urls import path

from ..views.hotel_room_views import HotelRoomView
urlpatterns = [
    path('add/<int:hotel_id>',HotelRoomView.add_hotel_room, name="add_hotel_room"),
    path('get/<int:room_id>', HotelRoomView.get_hotel_room, name="get_hotel_room"),
    path('update/<int:room_id>', HotelRoomView.update_hotel_room, name="update_hotel_room"),
    path('activate/<int:room_id>', HotelRoomView.activate_hotel_room, name="activate_hotel_room"),
    path('deactivate/<int:room_id>', HotelRoomView.deactivate_hotel_room, name="deactivate_hotel_room"),
]
