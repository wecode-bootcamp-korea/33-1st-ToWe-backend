import json, bcrypt

from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ValidationError

from .models import User
from .validator import validate_email, validate_password

class SignupView(View):
    def post(self, request):
        
        try :
            signup_data = json.loads(request.body)
            email       = signup_data["email"]
            password    = signup_data["password"]
            
            if not validate_email(email) :
                raise ValidationError("INVALID_EMAIL")

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