from django.views import View

from towe.utils import login_decorator
from .models import Cart

class CartView(View):
    @login_decorator
    def delete(self, request, cart_id):

        pass