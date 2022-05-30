from django.http import JsonResponse
from django.views import View
from django.db.models import Q

from products.models import Product


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
            'age_low'   : 'target_age_id__age'
        }

        if not sort_dict.get(sort):
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)  
        
        q = Q()

        if category:
            q &= Q(category__name=category)

        if search:
            q &= Q(name__contains=search)
        
        products = Product.objects.filter(q).order_by(sort_dict[sort])[offset:offset+limit]

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
        