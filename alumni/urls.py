from django.urls import path 
from .views import alumni_home 

urlpatterns = [
    path('/',alumni_home)
]