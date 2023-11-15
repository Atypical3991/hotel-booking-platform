import logging

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser

from ..models.SessionsModel import Sessions
from ..serializers.APIResponseSerializers import GetHotelierProfileByIdSerializer
from ..serializers.HotelierManagerAPIModelSerializers import *
from ..utils import JwtTokenUtil
from ..utils.wrappers import authentication_decorator


class HotelierManagerViews:
    logger = logging.getLogger(__name__)

    @staticmethod
    @api_view(["POST"])
    def create_profile(request):
        # Parse the incoming JSON data
        data = JSONParser().parse(request)

        # Serialize the data
        serializer = CreateHotelierSerializer(data=data)

        # Validate and save the data
        if serializer.is_valid():
            try:
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            except Exception as e:
                HotelierManagerViews.logger.error(
                    f"create_profile, exception raised!! e: {str(e)}, request : {request}")
                return JsonResponse({"status": "failure", "error": "Something went wrong"}, status=500)

        return JsonResponse(serializer.errors, status=400)

    @staticmethod
    @api_view(["PUT"])
    @authentication_decorator
    def update_profile_by_id(request, id):
        # Using get_object_or_404 to raise a 404 response if the instance is not found
        hotelier_instance = get_object_or_404(Hotelier, id=id)

        # Parse the incoming JSON data
        data = JSONParser().parse(request)

        # Serialize the data
        serializer = UpdateHotelierSerializer(data=data, instance=hotelier_instance);

        # Validate and save the data
        if serializer.is_valid():
            try:
                serializer.save()
                return JsonResponse({"status": "success", "message": "Hotelier updated successfully"}, status=200)
            except Exception as e:
                HotelierManagerViews.logger.error(
                    f"update_profile_by_id, exception raised!! e: {str(e)}, request : {request}")
            return JsonResponse({"status": "failure", "error": "Something went wrong"}, status=500)

        return JsonResponse(serializer.errors, status=400)

    @staticmethod
    @api_view(["GET"])
    @authentication_decorator
    def get_profile_by_id():
        # Using get_object_or_404 to raise a 404 response if the instance is not found
        hotelier_instance = get_object_or_404(Hotelier, id=id)

        # serialize data
        serializer = GetHotelierProfileByIdSerializer(hotelier_instance)

        # validated and save the data
        if serializer.is_valid():
            try:
                return JsonResponse({"status": "success", "message": "Hotelier profile fetched successfully",
                                     "data": serializer.data, }, status=200)
            except Exception as e:
                HotelierManagerViews.logger.error(f"get_profile_by_id, exception raised!! e: {str(e)}, id: {id}")
                return JsonResponse({"status": "failure", "error": "Something went wrong"}, status=500)

        return JsonResponse(serializer.errors, status=400)

    @staticmethod
    @api_view(["PUT"])
    @authentication_decorator
    def deactivate_profile_by_id():
        # Using get_object_or_404 to raise a 404 response if the instance is not found
        hotelier_instance = get_object_or_404(Hotelier, id=id)

        # deactivate customer
        hotelier_instance.active = False
        try:
            hotelier_instance.save()
            return JsonResponse({"status": "success", "message": "Hotelier deactivated successfully"}, status=200)
        except Exception as e:
            HotelierManagerViews.logger.error(f"deactivate_profile_by_id, exception raised!! id:{id} e:{str(e)}")
            return JsonResponse({"status": "failure", "message": "Something went wrong"}, status=500)

    @staticmethod
    @api_view(["PUT"])
    @authentication_decorator
    def re_activate_profile_by_id():
        # Using get_object_or_404 to raise a 404 response if the instance is not found
        hotelier_instance = get_object_or_404(Hotelier, id=id)

        # deactivate customer
        hotelier_instance.active = True
        try:
            hotelier_instance.save()
            return JsonResponse({"status": "success", "message": "Hotelier re_activated successfully"}, status=200)
        except Exception as e:
            HotelierManagerViews.logger.error(f"deactivate_profile_by_id, exception raised!! id:{id} e:{str(e)}")
            return JsonResponse({"status": "failure", "message": "Something went wrong"}, status=500)

    @staticmethod
    @api_view(['POST'])
    def login(request):
        # Parse the incoming JSON data
        data = JSONParser().parse(request)

        # Serialize the data
        serializer = HotelierLoginSerializer(data=data)

        # validate login request
        if serializer.is_valid():
            validated_data = serializer.validated_data
            hotelier_instance = get_object_or_404(Hotelier, username=validated_data.get('username'),
                                                  password=validated_data.get('password'))

            # check if use is active or not
            if not hotelier_instance.active:
                return JsonResponse({"status": "failure", "error": "You account has been deactivated. please "
                                                                   "re-activate your account."}, status=400)
            try:
                # delete all past sessions associated with passed user_id and role
                Sessions.objects.filter(user_id=hotelier_instance.id, role='user').delete()

                # generate JWT token using user_id and role
                token = JwtTokenUtil.generate_jwt_token(hotelier_instance.id, 'hotelier')

                # create session with newly generated token
                Sessions.objects.create(user_id=hotelier_instance.id, token=token, role='user')
                return JsonResponse({"status": "success", "token": token}, status=200)
            except Exception as e:
                HotelierManagerViews.logger.error(f"login, exception raised!! e :{str(e)}")
                return JsonResponse({"status": "failure", "error": "Something went wrong"}, status=400)

        return JsonResponse(serializer.errors, status=400)

    @staticmethod
    @api_view(['POST'])
    @authentication_decorator
    def logout(request):
        # Parse the incoming JSON data
        data = JSONParser().parse(request)

        # Serialize the data
        serializer = HotelierLogoutSerializer(data=data)

        # validate login request
        if serializer.is_valid():
            validated_data = serializer.validated_data

            # extract auth data set inside authentication_decorator
            auth_data = getattr(request, "auth_data", None)
            if auth_data is None:
                return JsonResponse({"status": "failure", "error": "Auth data not found"}, status=400)

            # validate whether requested is eligible to perform this action
            if auth_data.get('user_id') != validated_data.get("user_id") or auth_data.get('role') != validated_data.get(
                    "role"):
                return JsonResponse({"status": "failure", "error": "you're unauthorised to perform this action."},
                                    status=401)

            # fetch sessions with passed user_id and role
            sessions = get_object_or_404(Sessions, user_id=validated_data.get("user_id"),
                                         role=validated_data.get('role'))

            # if no sessions present do nothing
            if sessions is None:
                # return if no sessions present with the passed user_id and role
                return JsonResponse({"status": "success", "message": "No sessions present"}, status=200)

            try:
                # delete all sessions for the passed user_id and role
                Sessions.objects.filter(user_id=validated_data.get('user_id'), role=validated_data.get('role')).delete()
                return JsonResponse({"status": "success", "message": "Customer logged put successfully."}, status=200)
            except Exception as e:
                HotelierManagerViews.logger.error(f"login, exception raised!! e :{str(e)}")
                return JsonResponse({"status": "failure", "error": "Something went wrong"}, status=400)

        return JsonResponse(serializer.errors, status=400)
