from rest_framework import viewsets,status,permissions
from apps.orders.models import Order, UserAddress
from apps.flowers.serializers import FlowerSerializer
from rest_framework.response import Response
from apps.orders.serializers import OrderSerializer

class UserAddressViewSet(viewsets.ModelViewSet):
    serializer_class = None

    def get_serializer_class(self):
        from apps.orders.serializers import UserAddressSerializer  # Ленивый импорт
        return UserAddressSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return UserAddress.objects.filter(user_id=user_id)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
