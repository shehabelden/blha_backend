from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from auth_app.models import *
from prodact.serilezer import *
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','password',"email")
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['password'])
        return user
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")
class UserSer(serializers.ModelSerializer):
    product=ProductSerializer(many=True,read_only= True)
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields ="__all__"
class ProfileSerializer(serializers.ModelSerializer):
    user=UserSer(read_only= True)
    class Meta:
        model = Profile
        look_up="user"
        fields = "__all__"