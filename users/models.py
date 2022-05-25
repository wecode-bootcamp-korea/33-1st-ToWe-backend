from django.db import models

from core.models import TimeStampModel

class User(TimeStampModel):
    name         = models.CharField(max_length = 45)
    email        = models.CharField(max_length = 45, unique = True)
    password     = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 45)
    address      = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'users'

class Like(TimeStampModel):
    user_id    = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey("products.Product", on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'