from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CareerSerializer
from .models import Career


class CareerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
