from rest_framework import serializers
from .models import Vazifa2


class Vazifa2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vazifa2
        fields = '__all__'
