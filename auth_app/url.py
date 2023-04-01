from django.urls import path
from .api import *
urlpatterns = [
    path('login',LoginAPI.as_view()),
    path('signup', RegistrationAPI.as_view()),
    path('prof/<int:user>', ProfileApi.as_view()),
    path('use/<int:user>', MainUser.as_view()),
]