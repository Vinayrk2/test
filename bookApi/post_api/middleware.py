from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from useraccount.models import ApplicationUser

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('Authorization')
        if not api_key:
            raise AuthenticationFailed('API key missing.')

        try:
            user = ApplicationUser.objects.get(api_key=api_key)
        except:
            raise AuthenticationFailed('Invalid API key.')

        return (user, None)
