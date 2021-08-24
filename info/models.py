from django.db import connection, models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.reverse_related import OneToOneRel
# Create your models here.

class profilee(models.Model):
    connection=models.OneToOneField(to=User,on_delete=CASCADE)
    name = models.CharField(max_length=30,null=True,blank=True)
    profile_pic=models.ImageField(upload_to="pic",null=True,blank=True)
    profesion=models.CharField(max_length=30,null=True,blank=True)
    intro=models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    Dob= models.DateField(null=True,blank=True)
    city=models.CharField(max_length=20,null=True,blank=True)
    university=models.CharField(max_length=50,null=True,blank=True)
    website=models.CharField(max_length=30,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    degree=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=30,null=True,blank=True)
    phone=models.CharField(max_length=10,null=True,blank=True)

class services(models.Model):
    connection=models.ForeignKey(to=User,on_delete=CASCADE)
    title = models.CharField(max_length=20,null=True,blank=True)
    services_description=models.TextField(null=True,blank=True)
    services_icon=models.TextField(null=True,blank=True)

class technical_skills(models.Model):
    connection=models.ForeignKey(to=User,on_delete=CASCADE)
    tech_name= models.CharField(max_length=20,null=True,blank=True)
    progress=models.IntegerField(null=True,blank=True)

class professional_skills(models.Model):
    connection=models.ForeignKey(to=User,on_delete=CASCADE)
    profession_name= models.CharField(max_length=20,null=True,blank=True)
    progress=models.IntegerField(null=True,blank=True)

class portfollio(models.Model):
    connection=models.ForeignKey(to=User,on_delete=CASCADE)
    gallary=models.ImageField(upload_to='gallary',null=True,blank=True)

class contact(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=20,null=True,blank=True)
    phone=models.CharField(max_length=10,null=True,blank=True)
    message=models.TextField(null=True,blank=True)

class com(models.Model):
    connection=models.ForeignKey(to=User,on_delete=CASCADE)
    name=models.CharField(max_length=20,null=True,blank=True)
    profession=models.CharField(max_length=20,null=True,blank=True)
    message=models.TextField(null=True,blank=True)
