from django.views import View
from django.http import JsonResponse

from .models import Cart
from towe.utils import login_decorator

class CartView(View):
    @login_decorator
    def get(self, request):
        
        result = []
        for cart in Cart.objects.filter(user_id=request.user.id):
            product = cart.product
            result.append({
                'id':cart.id,
                'product_name':cart.product.product.name,
                'color':cart.product.color.color,
                'price':cart.product.product.price,
                'thumbnail_url':cart.product.product.thumbnail_img_url
            })
        
        return JsonResponse({'result':result}, status=200)