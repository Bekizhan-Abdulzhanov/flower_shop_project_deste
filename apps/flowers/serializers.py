from rest_framework import serializers
from apps.flowers.models import Flower, FlowerImage
from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer

class FlowerImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlowerImage
        fields = '__all__'

class FlowerSerializer(serializers.ModelSerializer):
    prog_img = FlowerImageSerializer(read_only = True,many=True)
    tag = CategorySerializer(read_only = True,many = True)
    
    class Meta:
        model = Flower
        fields = ['id', 'title', 'description', 'price','tag','prog_img',]


class FlowerCreateSerializer(serializers.ModelSerializer):
    prog_img = FlowerImageSerializer(many=True)
    class Meta:
        model = Flower
        fields = ['title', 'description', 'price','prog_img']

    