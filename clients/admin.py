from django.contrib import admin
from .models import Client, Worker


admin.site.register(Client)
admin.site.register(Worker)


