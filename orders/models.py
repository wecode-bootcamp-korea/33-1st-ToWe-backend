from django.db import models

from core.models import TimeStampModel

class OrderStates(models.Model):
    state = models.CharField(max_length=45)

    class Meta:
        db_table = 'order_states'

class Order(TimeStampModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'orders'

class OrderDetail(TimeStampModel):
    order          = models.ForeignKey("orders.Order", on_delete=models.CASCADE)
    product_option = models.ForeignKey("products.ProductOption", on_delete=models.CASCADE)
    order_state    = models.ForeignKey("orders.OrderStates", on_delete=models.CASCADE)
    quantity       = models.IntegerField()
    
    class Meta:
        db_table = 'order_details'