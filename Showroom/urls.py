from django.urls import path 
from . import views

app_name = 'Showroom'
urlpatterns = [
    path("" , views.brand_list , name ='brand_list'),
    path("<int:profile_id>" , views.brand_detail , name ='brand_detail'),
    path("team/" , views.our_team , name ='our_team'),
    path("Showrooms.html/" , views.showroomss , name ='showroomss'),

]
