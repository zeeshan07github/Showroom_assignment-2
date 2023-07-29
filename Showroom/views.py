from django.shortcuts import render
from .models import *

def brand_list(request):
    brands = brand.objects.all()
    return render(request, "Showroom/brand_list.html", {'brands': brands})

def brand_detail(request, profile_id):
    
        brandss = brand.objects.get(id=profile_id)
        models = brandss.models.all()
        

        return render(request, "Showroom/brand_detail.html", {'brandss': brandss, "models": models })

def our_team(request):
    team=staff.objects.all()
    return render(request , "Showroom/our_team.html",{'team':team})

def showroomss(request):
    Showroom=showroom.objects.all()
    return render(request ,  "Showroom/Showrooms.html", {'Showroom': Showroom})