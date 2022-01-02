from rest_framework import serializers
from .models import Weatherapi


class Weatherapiserializer(serializers,Serializer):
    class meta:
        model = Weatherapi
        fields = '__all__'

