import json

from django.views import View
from django.http import JsonResponse

from .models import Cart
from products.models import Product, ProductOption
from towe.utils import login_decorator

class CartView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)

        optioned_product = ProductOption.objects.get(product_id = data["product_id"], color_id=data["color_id"])

        cart, is_created = Cart.objects.get_or_create(
            user       = request.user,
            product_id = optioned_product.id,
            defaults   = {'quantity' : data["quantity"]},
        )

        if not is_created :
            cart.quantity += data["quantity"]
            cart.save()

        return JsonResponse({"MESSAGE":"SUCCESS"}, status=200)