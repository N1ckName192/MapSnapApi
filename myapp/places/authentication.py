from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class QueryParamTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get('token')
        if not token:
            return None  # Возвращаем None, если токен не предоставлен

        try:
            token_object = Token.objects.get(key=token)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        return (token_object.user, token_object)  # Возвращаем пользователя и токен
