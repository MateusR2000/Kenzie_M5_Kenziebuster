from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) 
    username = serializers.CharField(
        max_length=150,
        validators = [
            UniqueValidator(User.objects.all(), "username already taken."),
        ],
    )
    password = serializers.CharField(max_length=128, write_only=True)
    is_superuser = serializers.BooleanField(default=False)
    email = serializers.CharField(
        max_length=127,
        validators = [
            UniqueValidator(User.objects.all(), "email already registered.")
        ],
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(
        default=None
    )
    is_employee = serializers.BooleanField(default=False)

    def create(self, validated_data):
        if validated_data["is_superuser"]:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)

        return user
    
    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if(key=="password"):
                instance.set_password(value)
        instance.save()

        return instance

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)