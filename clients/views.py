from .models import Worker, Client
from .serializers import WorkerSerializer, ClientSerializer
from rest_framework import viewsets
from .utils import assign_available_worker  # или куда ты положишь функцию
import locale

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        worker = assign_available_worker()
        serializer.save(appointed_worker=worker)