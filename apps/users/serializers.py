from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'photo',
            'phone_number',
            'gender',
            'age', 
        ]

class SignUPSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'photo',
            'phone_number',
            'gender',
            'age',
            'password', 
        ]

    def create(self,validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
    
class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2=serializers.CharField(write_only=True,required=True)
    old_password=serializers.CharField(write_only=True,required=True)

    class Meta:
        model = User
        fields = ('old_password','password','password2')

    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Поля пароля не совпадают."})

        return attrs
    
    def validate_old_password(self,value):
        user=self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({'old_password':"Старый пароль неверен"})
        return value
    

    def save(self,**kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['password'])
        user.save()
        return user