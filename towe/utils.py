import jwt

from django.http import JsonResponse
from django.conf import settings

from users.models import User

def login_decorator(func):
    def wrapper(self, request, *args, **kargs):
        try:
            token = request.headers.get('Authorization')
            payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
            request.user = User.objects.get(id=payload['id'])

            return func(self, request, *args, **kargs)
        
        except User.DoesNotExist:
            return JsonResponse({"MESSAGE":"INVALID_USER"}, status=400)
        
        except jwt.exceptions.DecodeError:
            return JsonResponse({"MESSAGE":"INVALID_TOKEN"}, status=401)

        except jwt.ExpiredSignatureError:
            return JsonResponse({"MESSAGE":"EXPIRED_TOKEN"}, status=401)
        
    return wrapper