#Goggle-photos

from django.urls import path
#from django.conf.urls import re_path
from GooglePhotos import views

urlpatterns=[
      path('photos/',views.photo),
      path('photos-homepage/',views.show),
      
      
    ]
