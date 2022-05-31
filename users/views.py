import json
from datetime import datetime, timedelta

import jwt
import bcrypt
from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.conf import settings

from .models import User
from towe.utils import login_decorator
from .validator import validate_email, validate_password

class SignupView(View):
    def post(self, request):
        
        try :
            signup_data = json.loads(request.body)
            email       = signup_data["email"]
            password    = signup_data["password"]
            
            validate_email(email)
            validate_password(password)

            if not validate_password(password) :
                raise ValidationError("INVALID_PASSWORD")
            
            if User.objects.filter(email=email).exists() :
                raise ValidationError("EMAIL_ALREADY_EXIST")
            
            hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            User.objects.create(
                name         = signup_data["name"],
                email        = email,
                password     = hashed_pw.decode('utf-8'),
                phone_number = signup_data["phone_number"],
                address      = signup_data["address"]
                )

            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except KeyError :
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)

        except ValidationError as verr :
            return JsonResponse({"MESSAGE": verr.message}, status=400)

class LoginView(View):
    def post(self, request):
        
        try :
            login_data = json.loads(request.body)
            email      = login_data["email"]
            password   = login_data["password"]
            user       = User.objects.get(email=email)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')) :
                raise ValidationError("INCORRECT_PASSWORD")

            token = jwt.encode( {'id': user.id, 'exp': datetime.utcnow()+timedelta(days=3)}, settings.SECRET_KEY, settings.ALGORITHM)

            return JsonResponse({"TOKEN": token}, status=201)

        except KeyError :
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)
        
        except User.DoesNotExist :
            return JsonResponse({"MESSAGE": "INVALID_USER"}, status=400)

        except ValidationError as verr :
            return JsonResponse({"MESSAGE": verr.message}, status=400)

class UserDetailView(View):
    @login_decorator
    def get(self, request):
        
        user = request.user
        result = {
            'id'          : user.id,
            'email'       : user.email,
            'name'        : user.name,
            'phone_number': user.phone_number,
            'address'     : user.address
        }

        return JsonResponse({"result":result}, status=200)
