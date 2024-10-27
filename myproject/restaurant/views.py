from rest_framework import viewsets
from .models import Category, Product, Extra, Drinks, Contact
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ExtraSerializer,
    DrinksSerializer,
    ContactSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ExtraViewSet(viewsets.ModelViewSet):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer


class DrinksViewSet(viewsets.ModelViewSet):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer




class LocationView(APIView):
    def get(self, request):
        location = Location.objects.filter(name="Bishkek").first()
        serializer = LocationSerializer(location)
        return Response(serializer.data)
