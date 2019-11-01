from django.shortcuts import render
from rest_framework import generics
from .serializers import CarDetailSerializer, CarListSerializer
from .models import Car
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser, )
    # # If we want perm for admin and authentificate
    # permission_classes = (IsAuthenticated, IsAdminUser)


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    # # Add auth with token
    # # But we used another way -ADD REST_FRAMEWORK in settings
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (IsOwnerOrReadOnly, )
