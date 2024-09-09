from rest_framework import serializers
from apps.carts.models import Cart,CartItem
from apps.flowers.serializers import FlowerSerializer
from apps.flowers.models import Flower

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            "item", 
            "quantity",
        ]
    
    def create(self, validated_data):
        cart_item = super().create(validated_data)
        user = self.context["request"].user
        cart = Cart.objects.get(user=user)
        cart_item.cart = cart

        return cart_item

class AddCartItemSerializer(serializers.ModelSerializer):
    flower_id = serializers.UUIDField()

    def validate_flower_id(self, value):
        if not Flower.objects.filter(pk=value).exists():
            raise serializers.ValidationError("There is no product associated with the given ID")
        
        return value
    
    def save(self,**kwargs):
        cart_id = self._context['cart_id']
        product_id = self.validated_data ['flower_id']
        quantity = self.validated_data["quantity"] 
        
        try:
            cartitem = CartItem.objects.get(product_id=product_id, cart_id=cart_id)
            cartitem.quantity += quantity
            cartitem.save()
            
            self.instance = cartitem

        except:

            self.intance = CartItem.objects.create(cart_id = cart_id, **self.validated_data)

        return self.instance


    class Meta: 
    
        model = CartItem
        fileds = ['id','ite','quantity']

class CartSerializer(serializers.ModelSerializer):
    cart_item = CartItemSerializer(many=True, read_only=True, source='cart_flower')
    
    class Meta: 
        model = Cart 
        fields = [  
            'id',
            'cart_item',
        ]


