import json

from django.views import View
from django.http import JsonResponse

from .models import User

class SignupView(View):
    def post(self, request):
        
        try:
            data = json.loads(request.body)

            User.objects.create(
                name =
                email =
                password =
                phone_number =
                address =
            )


