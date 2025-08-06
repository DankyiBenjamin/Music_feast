from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

# Create your views here.
# createapiview gives a generic form to create a new room 
# listapiview gives a generic form to list all rooms
# ListCreateAPIView is a combination of both, allowing you to list all rooms and create a new room in one view
class RoomView(generics.ListAPIView):
    # a queryset is a collection of database records that can be filtered, ordered, and manipulated
    queryset = Room.objects.all()
    serializer_class = RoomSerializer