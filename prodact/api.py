from .serilezer import *
from .models import *
from rest_framework import mixins, generics
class ProductsApi(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class ProductApi(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = OneProductSerializer
    lookup_field="id"
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
class CategoriesApi(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
class CategorieApi(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = OneCategorySerializer
    lookup_field="id"
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)