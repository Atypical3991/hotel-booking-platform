from django.http import HttpResponse


def http_method_list(methods):
    def http_methods_decorator(func):
        def function_wrapper(self, request, **kwargs):
            methods_list = [method.upper() for method in methods]
            if not request.method.upper() in methods_list:
                return HttpResponse(status=405)  # not allowed

            return func(self, request, **kwargs)

        return function_wrapper

    return http_methods_decorator
