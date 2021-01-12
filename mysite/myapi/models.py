from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    item = models.CharField(max_length=20)
    amount = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item
