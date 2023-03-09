from django.db import models

# Create your models here.
class admindb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="pic", null=True, blank=True)

class itemdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="pic", null=True, blank=True)

class productdb(models.Model):
    category = models.CharField(max_length=100, null=True, blank=True)
    productname = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="pic", null=True, blank=True)

class admin(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank= True)



