from django.db import models

# Create your models here.
class Farmer(models.Model):
    name = models.CharField(max_length=150, null=True)
    address = models.TextField() 

    def __str__(self):
        return self.name

    