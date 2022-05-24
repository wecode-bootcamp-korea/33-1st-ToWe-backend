from django.db import models

from core.models import TimeStampModel
# from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class TargetAge(models.Model):
    age = models.IntegerField()

    class Meta:
        db_table = 'target_ages'

class Product(TimeStampModel):
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    target_age  = models.ForeignKey(Target_age, on_delete=models.SET_NULL, null=True)
    name        = models.CharField(max_length=45)
    price       = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    thumbnail   = models.CharField(max_length=260)

    class Meta:
        db_table = 'products'

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url     = models.CharField(max_length=260)

    class Meta:
        db_table = 'images'

class Color(models.Model):
    color = models.CharField(max_length=20)

    class Meta:
        db_table = 'colors'

class Review(TimeStampModel):
    user    = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        db_table = 'reviews'

class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color   = models.ForeignKey(Color, on_delete=models.CASCADE)
    stock   = models.IntegerField()

    class Meta:
        db_table = 'product_options'