from rest_framework import viewsets, permissions
from apps.flowers.models import Flower, FlowerImage
from apps.flowers.serializers import FlowerSerializer, FlowerImageSerializer, FlowerCreateSerializer

class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['create','update']:
            return FlowerCreateSerializer
        return FlowerSerializer

class FlowerImageViewSet(viewsets.ModelViewSet):
    queryset = FlowerImage.objects.all()
    serializer_class = FlowerImageSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]