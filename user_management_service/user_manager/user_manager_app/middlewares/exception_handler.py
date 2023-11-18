from ..utils.ResonseHandler import CustomRESTResponseHandler


class GlobalExceptionHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        # Handle the exception here
        error_message = str(exception)
        return CustomRESTResponseHandler(data=None, message=None, status_m="failure", error=error_message, status=500)
