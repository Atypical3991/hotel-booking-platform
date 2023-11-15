from django.urls import path

from ..hotelier_manager_views import *

urlpatterns = [
    path('', HotelierManagerViews.create_profile),
    path('profile/<int:id>', HotelierManagerViews.get_profile_by_id),
    path('profile/update/<int:id>', HotelierManagerViews.update_profile_by_id),
    path('profile/deactivate/<int:id>', HotelierManagerViews.deactivate_profile_by_id),
    path('profile/re_activate/<int:id>', HotelierManagerViews.re_activate_profile_by_id)
]
