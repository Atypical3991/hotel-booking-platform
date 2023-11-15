from django.urls import path

from ..customer_manager_views import *

urlpatterns = [
    path('', CustomerManagerViews.create_profile),
    path('profile/<int:id>', CustomerManagerViews.get_profile_by_id),
    path('profile/update/<int:id>', CustomerManagerViews.update_profile_by_id),
    path('profile/deactivate/<int:id>', CustomerManagerViews.deactivate_profile_by_id),
    path('profile/re_activate/<int:id>', CustomerManagerViews.re_activate_profile_by_id)
]
