from rest_framework.serializers import ModelSerializer

from users.models               import User


class SignUpSerializer(ModelSerializer):
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # self.Meta.model.objects.create_user(**validated_data)
        return user
    
    class Meta:
        model        = User  # get_user_model()
        fields       = ['email', 'nickname', 'password']
        extra_kwargs = {'password' : {'write_only' : True}}