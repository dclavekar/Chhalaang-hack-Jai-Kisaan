from django.db import models

# Create your models here.
class FarmerPersonalDetails(models.Model):
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150 )
    phone = models.IntegerField()

    def __str__(self):
        return str(self.first_name) +" " + str(self.last_name)


class LandDetails(models.Model):
   
    farmer_no = models.IntegerField()
    farmer = models.OneToOneField(FarmerPersonalDetails, on_delete=models.CASCADE)
    address = models.TextField()
    area_given = models.FloatField()
    
    cordinate1_x = models.FloatField()
    cordinate1_y = models.FloatField()
    cordinate2_x = models.FloatField()
    cordinate2_y = models.FloatField()
    cordinate3_x = models.FloatField()
    cordinate3_y = models.FloatField()
    cordinate4_x = models.FloatField()
    cordinate4_y = models.FloatField()
    n=models.IntegerField(default=4) #no of edges of the land

    # soil_image = models.ImageField(upload_to='images/landDetails/soil_images')
    # crop_image  = models.ImageField(upload_to='images/landDetails/crop_images')

    def __str__(self):
        return "Land of: "+ str(self.farmer.first_name)