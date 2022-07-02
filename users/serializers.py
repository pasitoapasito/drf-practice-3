from unittest.util import _MAX_LENGTH
from rest_framework             import serializers
from rest_framework.serializers import ModelSerializer

from users.models               import User


class SignUpSerializer(ModelSerializer):
    email    = serializers.CharField(max_length=100, required=True)
    nickname = serializers.CharField(required=False)
    password = serializers.CharField(required=True, write_only=True)
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # self.Meta.model.objects.create_user(**validated_data)
        return user
    
    class Meta:
        model        = User  # get_user_model()
        fields       = ['email', 'nickname', 'password']
        extra_kwargs = {'password' : {'write_only' : True}}