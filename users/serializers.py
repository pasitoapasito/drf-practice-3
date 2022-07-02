import re

from rest_framework             import serializers
from rest_framework.serializers import ModelSerializer

from users.models               import User


class SignUpSerializer(ModelSerializer):
    
    def create(self, validated_data):
        email    = validated_data.get('email')
        password = validated_data.get('password')
            
        email_regexp    = '^\w+([\.-]?\w+)*@\w+(\.\w{2,3})+$'
        password_regexp = '\S{8,20}$'
        
        if not re.match(email_regexp, email):
            raise serializers.ValidationError('message : invalid email')
        
        if not re.match(password_regexp, password):
            raise serializers.ValidationError('message : invalid password')
        
        user = User.objects.create_user(**validated_data)  # self.Meta.model.objects.create_user(**validated_data)
        return user
    
    class Meta:
        model        = User  # get_user_model()
        fields       = ['email', 'nickname', 'password']
        extra_kwargs = {'password' : {'write_only' : True}}