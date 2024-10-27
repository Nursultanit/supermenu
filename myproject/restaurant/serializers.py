from rest_framework import serializers
from .models import Contact, Category, Product, Extra, Drinks
from rest_framework import serializers
from .models import Location


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = ['id', 'name', 'price']

class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id', 'name', 'volume', 'price']

class ProductSerializer(serializers.ModelSerializer):
    extras = ExtraSerializer(many=True, read_only=True)
    drinks = DrinksSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'extras', 'drinks']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'products']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'created_at', 'updated_at']




class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'address', 'latitude', 'longitude']

