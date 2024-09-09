from rest_framework import viewsets,status

from django.contrib.auth import get_user_model

from apps.users import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.SignUPSerializer
        return self.serializer_class
    

class ChangePasswordViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def update(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'detail':'Пароль успешно обновлен'},status=status.HTTP_200_OK)
    

    def perform_update(self, serializer):
        serializer.save()