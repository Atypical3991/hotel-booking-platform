from django.http import JsonResponse


class CustomRESTResponseHandler(JsonResponse):
    def __init__(self, data, status_m, message, error, **kwargs):
        super().__init__({"data": data, "status": status_m, "message": message, "error": error}, **kwargs)
