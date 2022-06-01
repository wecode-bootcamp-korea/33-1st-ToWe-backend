import json

from django.http import JsonResponse
from django.views import View
from django.db.models import Q, Count

from products.models import Product, Review
from users.models import LikeProduct
from towe.utils import login_decorator

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id = product_id)
            images  = [image.url for image in product.imageurl_set.all()]
            colors  = [{
                'color_id' : productoption.color.id,
                'color': productoption.color.color
            } for productoption in product.productoption_set.all()]
            product_detail = {
                'product_id' : product.id,
                'name'       : product.name,
                'price'      : product.price,
                'description': product.description,
                'image_url'  : images,
                'colors'      : colors,
            }
            
            return JsonResponse({'results': product_detail}, status =200)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'DOES_NOT_EXIST'}, status = 400)
           
class ProductListView(View):
    def get(self, request):        
        category = request.GET.get('category')
        sort     = request.GET.get('sort', 'id')
        search   = request.GET.get('search')
        offset   = int(request.GET.get('offset', 0))
        limit    = int(request.GET.get('limit', 6))


        sort_dict = {
            'id'        : '-id',
            'price_high': '-price',
            'price_low' : 'price',
            'age_high'  : '-target_age_id__age',
            'age_low'   : 'target_age_id__age',
            'best'      : '-like_count'
        }

        if not sort_dict.get(sort):
            return JsonResponse({"MESSAGE": "SORT_KEY_ERROR"}, status=400)  
        
        q = Q()

        if category:
            q &= Q(category__name=category)

        if search:
            q &= Q(name__contains=search)
        
        products = Product.objects.filter(q).annotate(like_count=Count('likeproduct')).order_by(sort_dict[sort])[offset:offset+limit]

        product_list = [
            {
                "id"           : product.id,
                "name"         : product.name,
                "price"        : product.price,
                "thumbnail_url": product.thumbnail_img_url,
                "hover_img"    : product.imageurl_set.first().url,
            }      
            for product in products
        ]

        return JsonResponse({'results': product_list}, status = 200)

class LikeView(View):
    @login_decorator
    def put(self, request, product_id):
        try:
            user = request.user
            product = Product.objects.get(id = product_id)
            like, is_created = LikeProduct.objects.get_or_create(
                product_id = product.id,
                user_id = user.id 
            )
            
            if not is_created:
                like.delete()
                message = 'DELETED'
                status = 204
            else:
                like.save()
                message = 'CREATED'
                status = 201
                
            return JsonResponse({
                'message': message
            }, status=status)            

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({'message':'PRODUCT_DOES_NOT_EXIST'}, status=404)
        
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

