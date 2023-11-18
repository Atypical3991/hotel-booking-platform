from django.urls import path

from ..views.hotel_views import HotelView
urlpatterns = [
    path('add',HotelView.add_hotel, name="add_hotel"),
    path('get/<int:hotel_id>', HotelView.get_hotel, name="get_hotel"),
    path('update/<int:hotel_id>', HotelView.update_hotel, name="update_hotel"),
    path('activate/<int:hotel_id>', HotelView.activate_hotel, name="activate_hotel"),
    path('deactivate/<int:hotel_id>',HotelView.deactivate_hotel, name="deactivate_hotel"),
]
