from django.db import models

# Create your models here.

class EntryPass(models.Model):
    name = models.CharField(max_length=100, unique=True)
    place = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
