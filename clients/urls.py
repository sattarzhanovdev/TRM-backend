from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkerViewSet, ClientViewSet

router = DefaultRouter()
router.register(r'workers', WorkerViewSet)
router.register(r'clients', ClientViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
