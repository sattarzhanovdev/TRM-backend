from .models import Worker, Client
from .serializers import WorkerSerializer, ClientSerializer
from rest_framework import viewsets
import locale

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer