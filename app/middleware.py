from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class RedirectUnauthenticatedMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # List of paths that do not require authentication
        excluded_paths = ['/signin/', '/signup/']

        # Check if the user is not authenticated and the request path is not excluded
        if not request.user.is_authenticated and not any(request.path.startswith(path) for path in excluded_paths):
            return redirect('/signin/')
