#Google-notes

from django.urls import path
from django.urls import re_path
from GoogleNotes import views

urlpatterns=[
      path('notes/',views.note),
      path('notes-homepage/',views.show),
      #re_path('^.*$',views.homepage),
      
    ]

