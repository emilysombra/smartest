from django.shortcuts import render
from rest_framework import viewsets

from .models import Class
from .serializers import ClassSerializer


class ClassViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
