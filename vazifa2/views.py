from rest_framework.viewsets import ModelViewSet
from .models import Vazifa2
from .serializers import Vazifa2Serializer


class Vazifa2ViewSet(ModelViewSet):
    queryset = Vazifa2.objects.all()
    serializer_class = Vazifa2Serializer
