from django.db import models

class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    appointed_worker = models.CharField(max_length=255)
    payment = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default="Не оплачено")