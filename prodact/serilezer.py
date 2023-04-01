from rest_framework import serializers
from .models import *
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"
class OneCategorySerializer(serializers.ModelSerializer):
        class Meta:
         model = CategoryModel
         look_up="id"
         depth=1
         fields = ["id","image","product"]
class OneProductSerializer(serializers.ModelSerializer):
    catrgory=CategorySerializer(read_only= True)
    class Meta:
        model = ProductModel
        look_up="id"
        fields = "__all__"
class ProductSerializer(serializers.ModelSerializer):
    catrgory=CategorySerializer(read_only= True)
    class Meta:
        model = ProductModel
        fields = "__all__"
