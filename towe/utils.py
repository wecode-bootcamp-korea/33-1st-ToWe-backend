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
        
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message': 'INVALID_TOKEN'}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({'message': 'NOT_EXIST_USER'}, status=400)

        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'EXPIRED_TOKEN'}, status=400)
    
    return wrapper