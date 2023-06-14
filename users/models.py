from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username