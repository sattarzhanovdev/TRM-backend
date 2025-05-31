from .models import Client, Worker
from django.db.models import Count, Q  # не забудь Q

def assign_available_worker():
    # Получаем работников с количеством активных клиентов (например, "Ожидание")
    workers_with_count = Worker.objects.annotate(
        active_clients=Count('client', filter=Q(client__status='Ожидание'))
    ).order_by('active_clients')

    if workers_with_count.exists():
        return workers_with_count.first()
    return None
