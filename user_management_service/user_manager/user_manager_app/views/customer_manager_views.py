import logging

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser

from ..models.CustomerModel import Customer
from ..serializers.APIResponseSerializers import GetCustomerProfileByIdSerializer
from ..serializers.CustomerManagerAPIModelSerializers import CreateCustomerSerializer, UpdateCustomerSerializer


class CustomerManagerViews:
    logger = logging.getLogger(__name__)

    @staticmethod
    @api_view(["POST"])
    def create_profile(request):
        # Parse the incoming JSON data
        data = JSONParser().parse(request)

        # Serialize the data
        serializer = CreateCustomerSerializer(data=data)

        # Validate and save the data
        if serializer.is_valid():
            try:
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            except Exception as e:
                CustomerManagerViews.logger.error(
                    f"create_profile, exception raised!! e: {str(e)}, request : {request}")
                return JsonResponse({"status": "failure", "error": "Something went wrong"}, status=500)

        return JsonResponse(serializer.errors, status=400)

    @staticmethod
    @api_view(["PUT"])
    def update_profile_by_id(request, id):
        # Using get_object_or_404 to raise a 404 response if the instance is not found
        customer_instance = get_object_or_404(Customer, id=id)

        # Parse the incoming JSON data
        data = JSONParser().parse(request)

        # Serialize the data
        serializer = UpdateCustomerSerializer(data=data, instance=customer_instance);

        # Validate and save the data
        if serializer.is_valid():
            try:
                serializer.save()
                return JsonResponse({"status": "success", "message": "Customer updated successfully"}, status=200)
            except Exception as e:
                CustomerManagerViews.logger.error(
                    f"update_profile_by_id, exception raised!! e: {str(e)}, request : {request}")
            return JsonResponse({"status": "failure", "error": "Something went wrong"}, status=500)

        return JsonResponse(serializer.errors, status=400)

    @staticmethod
    @api_view(["GET"])
    def get_profile_by_id(request, id):
        # Using get_object_or_404 to raise a 404 response if the instance is not found
        customer_instance = get_object_or_404(Customer, id=id)

        # serialize data
        serializer = GetCustomerProfileByIdSerializer(customer_instance)

        # validated and save the data
        if serializer.is_valid():
            try:
                return JsonResponse({"status": "success", "message": "Customer profile fetched successfully",
                                     "data": serializer.data, }, status=200)
            except Exception as e:
                CustomerManagerViews.logger.error(f"get_profile_by_id, exception raised!! e: {str(e)}, id: {id}")
                return JsonResponse({"status": "failure", "error": "Something went wrong"}, status=500)

        return JsonResponse(serializer.errors, status=400)

    @staticmethod
    @api_view(["PUT"])
    def deactivate_profile_by_id(request, id):
        # Using get_object_or_404 to raise a 404 response if the instance is not found
        customer_instance = get_object_or_404(Customer, id=id)

        # deactivate customer
        customer_instance.active = False
        try:
            customer_instance.save()
            return JsonResponse({"status": "success", "message": "Customer deactivated successfully"}, status=200)
        except Exception as e:
            CustomerManagerViews.logger.error(f"deactivate_profile_by_id, exception raised!! id:{id} e:{str(e)}")
            return JsonResponse({"status": "failure", "message": "Something went wrong"}, status=500)

    @staticmethod
    @api_view(["PUT"])
    def re_activate_profile_by_id(request, id):
        # Using get_object_or_404 to raise a 404 response if the instance is not found
        customer_instance = get_object_or_404(Customer, id=id)

        # deactivate customer
        customer_instance.active = True
        try:
            customer_instance.save()
            return JsonResponse({"status": "success", "message": "Customer re_activated successfully"}, status=200)
        except Exception as e:
            CustomerManagerViews.logger.error(f"deactivate_profile_by_id, exception raised!! id:{id} e:{str(e)}")
            return JsonResponse({"status": "failure", "message": "Something went wrong"}, status=500)
