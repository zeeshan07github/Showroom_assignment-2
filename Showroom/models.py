from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.

class staff(models.Model):
    name = models.CharField(max_length=50)
    Role = models.CharField(max_length=50 ,null = True )
    image = models.ImageField(null = True , blank = True)
    def __str__(self):
        return self.name


class feature(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    
class showroom(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True , blank= True)
    Location = models.CharField(max_length=50)
    contact = models.EmailField(max_length=254 , null = True)
    Owner = models.CharField( max_length=50)
    Staff = models.ManyToManyField(staff)

    
    def __str__(self):
        return self.name
    
class brand(models.Model):
    name = models.CharField(max_length=50)
    Logo = models.ImageField(null = True , blank = True)
    showrooms = models.ForeignKey(showroom,on_delete=models.CASCADE, null= True)
    def __str__(self):
        return self.name

class Engine_model(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class engine(models.Model):
    name = models.CharField(max_length=50)
    Engine_no = models.CharField(max_length=50,primary_key=True)
    model = models.ForeignKey(Engine_model,verbose_name=('Engine model name'),related_name='model', on_delete=models.CASCADE, null= True)
    def __str__(self):
        return self.name
      

class model(models.Model):
    name = models.CharField(max_length=50)
    images = models.ImageField(null=True,blank=True, storage=fs)
    Brand = models.ForeignKey(brand, related_name='models', on_delete=models.CASCADE, null=True)
    Engine = models.OneToOneField(engine, related_name='model_model', on_delete=models.CASCADE, null=True)  # Change the related name here
    Features = models.ManyToManyField(feature, related_name='models')
    
    def __str__(self):
        return self.name

class car(models.Model):
    model =models.ForeignKey(model, on_delete=models.CASCADE , null = True)
    Chasis_no = models.CharField(max_length=50 , primary_key=True)
    
    def __str__(self):
        return self.Chasis_no
       

 


