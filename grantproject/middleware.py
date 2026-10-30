# Language middleware: keeps the active language in the session.
# Based on a third-party snippet (ninja.uz).

from django.conf import settings
from django.utils import translation


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.session.get('lang') not in dict(settings.LANGUAGES):
            request.session['lang'] = 'uz'
        translation.activate(request.session['lang'])
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
