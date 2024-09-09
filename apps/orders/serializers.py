from rest_framework import serializers
from apps.orders.models import Order, UserAddress,OrderItem
from apps.flowers.serializers import FlowerSerializer
from apps.flowers.models import Flower
from apps.carts.models import Cart,CartItem

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['id', 'city_status', 'street', 'home']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        user_address = UserAddress.objects.create(user=user, **validated_data)
        return user_address
    
    def validate(self, attrs):
        return super().validate(attrs)
    
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.orders.models import Order, UserAddress
from apps.flowers.serializers import FlowerSerializer

class OrderSerializer(serializers.ModelSerializer):
    user_address = serializers.PrimaryKeyRelatedField(queryset=UserAddress.objects.all())
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all(), required=False, allow_null=True)

    
    class Meta:
        model = Order
        fields = ('id', 'user_address', 'flower','cart','order_status')
        read_only_fields = ('id', 'order_status',)

    def validate(self, data):
        user_address = data['user_address']
        user_id = self.context['request'].user.id

        if user_address.user_id != user_id:
            raise ValidationError(detail='Address not found')

        return data

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        cart = validated_data.get('cart')
        order = Order.objects.create(user_id=user_id, **validated_data)

        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                pass

            cart.cart_flower.all().delete()

        return order
    
class OrderItemSerializer(serializers.ModelSerializer):
    flower = FlowerSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'flower', 'quantity']