from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes),
    path('farmers/', views.getAllFarmers),
    path('farmer/<str:pk>', views.getFarmers),
    path('farmer/create/', views.createFarmer),
    path('farmer/update/<str:pk>', views.updateFarmer),
    path('farmer/delete/<str:pk>', views.deleteFarmer),
]
