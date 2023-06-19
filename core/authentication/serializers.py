from .models import User, Role
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model= User
        fields= ('id','email','password','first_name','last_name','phone_number','rol')
        #hide pass to return instance
        extra_kwargs = {
            'password': {'write_only': True}
        }

    #encrypt pass when the user is created
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class RoleSerializer(ModelSerializer):

    class Meta:
        model= Role
        fields= '__all__'