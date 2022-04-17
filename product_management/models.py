from django.db import models
from swan_ecommerce.models import BaseModel
# from administraion.models import *

class ProductCategory(BaseModel):
    category    = models.CharField('Product Category', max_length=50, null=True, unique=True)

    def __str__(self):
        return (self.category)

def image_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.product_category.category,filename)

class Product(BaseModel):
    product_name        = models.CharField(max_length=100, null=True)
    thumbnail_image     = models.ImageField(upload_to= image_directory_path, null=True, blank=True)
    product_category    = models.ForeignKey(ProductCategory, on_delete= models.CASCADE, null=True)
    description         = models.TextField( null=True, blank=True)
    price               = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity            = models.IntegerField("Available Quantity", null=True)
    in_stock            = models.IntegerField("In Stock", null=True, blank=True)
    sold                = models.IntegerField("Total Sold", null=True, blank=True)

    def __str__(self):
        return (self.product_name)

    def save(self, *args, **kwargs):
        if self.quantity:
            self.in_stock = self.quantity
        super(Product, self).save(*args, **kwargs)