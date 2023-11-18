from django.http import HttpResponse, JsonResponse

from ..models.SessionsModel import Sessions
from ..utils import JwtTokenUtil


def http_method_list(methods):
    def http_methods_decorator(func):
        def function_wrapper(self, request, **kwargs):
            methods_list = [method.upper() for method in methods]
            if not request.method.upper() in methods_list:
                return HttpResponse(status=405)  # not allowed

            return func(self, request, **kwargs)

        return function_wrapper

    return http_methods_decorator


def authentication_decorator(func):
    def function_wrapper(request, *args, **kwargs):
        # extract
        authorization_header = request.META.get('HTTP_AUTHORIZATION', None)
        if authorization_header is None:
            return JsonResponse({"status": "failure", "error": "Please pass authentication token"}, status=400)

        session = Sessions.objects.filter(token=authorization_header).first()
        if session is None:
            return JsonResponse({"status": "failure", "error": "Invalid token."}, status=401)

        payload = JwtTokenUtil.decode_jwt_token(authorization_header)
        if payload is None:
            return JsonResponse({"status": "failure", "error": "Authentication failed."}, status=401)
        setattr(request, "auth_data", payload)
        return func(request, *args, **kwargs)

    return function_wrapper
