from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dummy/', include('api.urls')),
    # path('info/', include('information.urls')),
    path('', include('jai_kisaan.urls')),
]
