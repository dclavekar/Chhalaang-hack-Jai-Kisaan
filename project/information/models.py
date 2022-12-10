# from django.db import models

# # Create your models here.





# class FarmerPersonalDetails(models.Model):

#     # gender_choice=(
#     #     ("Male","Male"),
#     #     ("Female","Female")
#     # )
#     # married_choice=( 
#     #     ("Yes","Yes"),
#     #     ("No","No")
#     # )
#     # dependent_choice = (
#     #     (0,"0"),
#     #     (1,"1"),
#     #     (2,"2"),
#     #     (3,"3") #dataset says 3+. string format
#     # )
#     # education_choice=(
#     #     ("Graduate","Graduate"),
#     #     ("Not Graduate","Not Graduate")
#     # )
#     # self_employed_choice = (
#     #     ("Yes","Yes"),
#     #     ("No","No")
#     # )
#     # credit_history_choice = (
#     #     (1,"1"),
#     #     (0,"0")
#     # )
#     # property_area_choice = (
#     #     ("Urban","Urban"),
#     #     ("Semiurban",'Semiurban'),
#     #     ("Rural","Rural")
#     # )
#     # loan_status_choice=(
#     #     ("Y","Y"),
#     #     ("N","N")
#     # )

#     first_name = models.CharField(max_length = 150)
#     last_name = models.CharField(max_length = 150 )
#     phone = models.IntegerField()
    
#     #prediction dataset variables:
#     # gender = models.CharField(max_length=20, choices=gender_choice)
#     # married = models.CharField(max_length=20, choices=married_choice)
#     # dependent = models.IntegerField( choices=dependent_choice)
#     # education = models.CharField(max_length=20,choices= education_choice)
#     # self_employed = models.CharField(max_length=20, choices=self_employed_choice)
#     # credit_history = models.IntegerField(choices=credit_history_choice)
#     # loan_status = models.CharField(max_length=20, choices=loan_status_choice)
#     # property_area = models.CharField(max_length=20,choices=property_area_choice)

#     # # loan_id = models.IntegerField(default=0)
#     # applicant_income = models.IntegerField()
#     # coapplicant_income = models.IntegerField()
#     # loan_amount = models.IntegerField()
#     # loan_amount_term = models.IntegerField()
    

#     def __str__(self):
#         return str(self.first_name) +" " + str(self.last_name)
    


# class LandDetails(models.Model):
   
#     farmer_no = models.IntegerField()
#     farmer = models.OneToOneField(FarmerPersonalDetails, on_delete=models.CASCADE)
#     address = models.TextField()
#     area_given = models.FloatField()
#     area_calculated = models.FloatField()
#     cordinate1_x = models.FloatField()
#     cordinate1_y = models.FloatField()
#     cordinate2_x = models.FloatField()
#     cordinate2_y = models.FloatField()
#     cordinate3_x = models.FloatField()
#     cordinate3_y = models.FloatField()
#     cordinate4_x = models.FloatField()
#     cordinate4_y = models.FloatField()
#     n=models.IntegerField(default=4) #no of edges of the land

#     soil_image = models.ImageField(upload_to='images/landDetails/soil_images')
#     crop_image  = models.ImageField(upload_to='images/landDetails/crop_images')

#     def __str__(self):
#         return "Land of: "+ str(self.farmer.first_name)

    


# class LandProperties(models.Model):
#     #add land object onetoone field
#     land =  models.OneToOneField( LandDetails, on_delete=models.CASCADE)
#     land_no = models.IntegerField()
#     crop_marketibility_choices = (
#     (1,"International"),
#     (2,"National"),
#     (3,"Domestic"),
#     )
#     crop_proposed_choices = (
#     (1, "Commercial"),
#     (2, "Traditional")
#     )
#     soil_fertility_choices =(
#     (1, "Good"),
#     (2, "Normal"),

#     (3, "Poor"),
#     )
#     enviromental_condition_choices =(
#     (1, "Good"),
#     (2, "Normal"),
#     (3, "Poor"),
#     )
#     market_location_choices =(
#     (1, "< 5km"),
#     (2, "< 10km"),
#     (3, "< 20"),
#     (4, "< 50"),
#     (5, "> 50"),
#     )
#     water_arrangement_choices =(
#     (1, "Good"),
#     (2, "Normal"),
#     (3, "Poor"),
#     )
#     transport_system_choices =(
#     (1, "Good"),
#     (2, "Normal"),
#     (3, "Poor"),
#     )
#     storage_system_choices =(
#     (1, "Good"),
#     (2, "Normal"),
#     (3, "Poor"),
#     )
#     machinery_availability_choices =(
#     (1, "Good"),
#     (2, "Normal"),
#     (3, "Poor"),
#     )
#     manpower_availability_choices =(
#     (1, "Good"),
#     (2, "Normal"),
#     (3, "Poor"),
#     )
#     fertility_classification_choices  =(
#     (1, "Fertile"),
#     (2, "Normal"),
#     (3, "Infertile")
#     )
#     farmer_repuation_locals_choices =(
#     (1, "Good"),
#     (2, "Normal"),
#     (3, "Poor"),
#     )
#     topography_choices =(
#    (1, "Good"),
#     (2, "Normal"),
#     (3, "Poor"),
#     )
#     seed_fertilizer_availability_choices=(
#    (1, "Good"),
#     (2, "Normal"),
#     (3, "Poor"),
#     )
#     govt_subsidy_availability_choices =(
#     (1, "Available"),
#     (2, "Can be arranged"),
#     (3, "Not available"),
#     )
#     technology_usage_choices = (
#     (1, "Good"),
#     (2, "Normal"),
#     (3, "Poor"),
#     )
#     method_of_cultivation_choices = (
#     (1, "Organic"),
#     (2, "Inorganic"),
#     (3, "Hybrid"),
# )
    
#     #here the factors store integer values corresponding to the strings
#     crop_marketibility =  models.IntegerField( choices = crop_marketibility_choices, default = 2)
#     crop_proposed =  models.IntegerField( choices = crop_proposed_choices, default = 2)
#     soil_fertility =  models.IntegerField( choices = soil_fertility_choices, default = 3)
#     enviromental_condition =  models.IntegerField( choices = enviromental_condition_choices, default = 3)
#     market_location =  models.IntegerField( choices = market_location_choices, default = 1)
#     water_arrangement =  models.IntegerField( choices = water_arrangement_choices, default = 2)
#     transport_system =  models.IntegerField( choices = transport_system_choices, default = 2)
#     storage_system =  models.IntegerField( choices = storage_system_choices, default = 2)
#     machinery_availability =  models.IntegerField( choices = machinery_availability_choices, default = 2)
#     manpower_availability =  models.IntegerField( choices = manpower_availability_choices, default = 2)
#     fertility_classification =  models.IntegerField( choices = fertility_classification_choices, default = 2)
#     farmer_repuation_locals =  models.IntegerField( choices = farmer_repuation_locals_choices, default = 2)
#     topography =  models.IntegerField( choices = topography_choices, default = 2)
#     seed_fertilizer_availability =  models.IntegerField( choices = seed_fertilizer_availability_choices, default = 2)
#     govt_subsidy_availability =  models.IntegerField( choices = govt_subsidy_availability_choices, default = 1)
#     technology_usage =  models.IntegerField( choices = technology_usage_choices, default = 2)
#     method_of_cultivation =  models.IntegerField( choices = method_of_cultivation_choices, default = 3)


#     def __str__(self):
#         # print("value of crop marketibility in integer")
#         # print(self.crop_marketibility)
#         return "Land no: " + str(self.land.pk) #change
       