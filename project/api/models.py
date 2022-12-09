from django.db import models

# Create your models here.
class Farmer(models.Model):
    name = models.CharField(max_length=150, null=True)
    address = models.TextField() 

    def __str__(self):
        return self.name

    

class Cart(models.Model):
    farmer = models.OneToOneField(Farmer, on_delete=models.CASCADE)
    cart_holds = models.CharField(max_length=120)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.cart_holds