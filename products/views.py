import json

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
    @login_decorator
    def post(self, request):
        try:
            data    = json.loads(request.body)
            product = Product.objects.get(id=data["product_id"])

            Review.objects.create(
                user    = request.user,
                product = product,
                content = data["content"])

            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)
        
        except Product.DoesNotExist:
            return JsonResponse({"MESSAGE":"PRODUCT_DOES_NOT_EXIST"}, status=400)

    @login_decorator
    def get(self, request):
        
        reviews = Review.objects.filter(user_id=request.user.id)
        result  = []
        for review in reviews:
            result.append({
                'review_id'   : review.id,
                'user_name'   : review.user.name,
                'product_name': review.product.name,
                'content'     : review.content,
                'created_at'  : review.created_at,
                'updated_at'  : review.updated_at
            })

        return JsonResponse({'result':result}, status=200)