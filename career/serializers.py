from rest_framework import serializers
from .models import Career


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ('id', 'title', 'description', 'reference')
