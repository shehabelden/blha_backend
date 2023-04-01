from django.urls import path
from .api import *

urlpatterns = [
    path('Product', ProductsApi.as_view()),
    path('Products/<int:id>', ProductApi.as_view()),
    path('', CategoriesApi.as_view()),
    path('<int:id>', CategorieApi.as_view())

]
