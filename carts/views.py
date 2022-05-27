import json

from django.views import View

from .models import Cart
from products.models import ProductOption
from towe.utils import login_decorator

class CartView(View):
    @login_decorator
    def post(self, request):

        data = json.loads(request.body)

        product_id = 
        color_id = 

        # product_option_id

        product = ProductOption.objects.filter(product_id=data["product_id"] and color_id=data["color_id"])

        user = request.user

        Cart.objects.create(
            user = request.user,
            product = product,
            quantity = quantity = data["quantity"]
        )
