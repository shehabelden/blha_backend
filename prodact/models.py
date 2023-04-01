from django.db import models

from django.db import models
from django.contrib.auth.models import User
class CategoryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    image = models.ImageField()
    rate = models.IntegerField(default=0)
    product = models.ManyToManyField(
        "ProductModel",
        null=True,
        blank=True,
    )

class ProductModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, )
    topic = models.CharField(max_length=400, )
    image = models.ImageField()
    bio = models.CharField(max_length=4000)
    rate = models.IntegerField()
    catrgory = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
