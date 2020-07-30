from django.db import models

# Create your models here.

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.email


