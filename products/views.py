from django.http import JsonResponse
from django.views import View

from products.models import Product


class ProductDetailView(View):
	def get(self, request, product_id):
		try:
			product = Product.objects.get(pk = product_id)
			images  = [image.url for image in product.imageurl_set.all()]
			colors  = [productoption.color.color for productoption in product.productoption_set.all()]

			product_detail = [
				{
					'product_id' : product.id,
					'name' : product.name,
					'price' : product.price,
					'description' : product.description,
					'image_url' : images,
					'color' :colors,

				}
			]
			return JsonResponse({'product_detail': product_detail}, status =200)
		except Product.DoesNotExist:
			return JsonResponse({'message': 'DOES_NOT_EXIST'}, status = 400)

