from django.db import models

from core.models import TimeStampModel
# from users.models import User
from products.models import ProductOption

class Cart(TimeStampModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'carts'