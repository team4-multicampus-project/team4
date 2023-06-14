from django.db import models
from django.contrib.auth.models import User

class Drink(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ml = models.CharField(max_length=255)

class Frige(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class FrigeItem(models.Model):
    frige = models.ForeignKey(Frige, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)