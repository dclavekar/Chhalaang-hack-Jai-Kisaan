from django.urls import path
from . import views

urlpatterns = [
   path('',views.homepage),
   path('getAllFarmers/',views.getAllFarmerPersonalDetails),
   # path('getAllFarmerNames/',views.getAllFarmerNames)
   path('getAllLands/',views.getAllLands),
   
   path('createFarmerPersonalDetails/',views.createFarmerPersonalDetails),
   path('createLandDetails/',views.createLandDetails),
   path('geolocation/',views.get_geolocation),
   path('getImages/',views.get_images),
   path('report/<int:primary_key>/',views.all_details_report),      
    
]