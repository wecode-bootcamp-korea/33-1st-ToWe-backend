import json

from django.views import View

from .models import Cart
from products.models import ProductOption
from towe.utils import login_decorator

class CartView(View):
    @login_decorator
    def post(self, request):

        data = json.loads(request.body)

        product_id = data["product_id"]
        quantity = data["quantity"]

        Pro
        user = request.user


        Cart.objects.create(
            user_id = user.id

        )
