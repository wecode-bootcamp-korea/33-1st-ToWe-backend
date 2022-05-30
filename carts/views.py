import json

from django.views import View
from django.http import JsonResponse

from .models import Cart
from products.models import ProductOption
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

    @login_decorator
    def get(self, request):
        
        result = []
        for cart in Cart.objects.filter(user_id=request.user.id):
            result.append({
                'cart_id'      : cart.id,
                'product_id'   : cart.product.product.id,
                'product_name' : cart.product.product.name,
                'color'        : cart.product.color.color,
                'price'        : cart.product.product.price,
                'quantity'     : cart.quantity,
                'thumbnail_url': cart.product.product.thumbnail_img_url
            })
        
        return JsonResponse({'result':result}, status=200)

    @login_decorator
    def delete(self, request, cart_id):

        cart = Cart.objects.get(id=cart_id)
        cart.delete()