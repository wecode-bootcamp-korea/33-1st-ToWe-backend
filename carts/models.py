from django.db import models

from core.models import TimeStampModel
from products.models import ProductOption

class Cart(TimeStampModel):
    user     = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product  = models.ForeignKey("products.ProductOption", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'carts'