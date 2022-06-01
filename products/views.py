from django.http import JsonResponse
from django.views import View

from products.models import Product, Review
from towe.utils import login_decorator

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id = product_id)
            images  = [image.url for image in product.imageurl_set.all()]
            colors  = [productoption.color.color for productoption in product.productoption_set.all()]
            product_detail = {
                'product_id' : product.id,
                'name'       : product.name,
                'price'      : product.price,
                'description': product.description,
                'image_url'  : images,
                'color'      : colors,
            }
            
            return JsonResponse({'results': product_detail}, status =200)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'DOES_NOT_EXIST'}, status = 400)

class ReviewView(View):
    def get(self, request, product_id):
    
        result = [{
            'review_id' : review.id,
            'user_name' : review.user.name,
            'content'   : review.content,
            'created_at': review.created_at,
            'updated_at': review.updated_at
        } for review in Review.objects.filter(product_id=product_id)]
    
        return JsonResponse({'result':result}, status=200)