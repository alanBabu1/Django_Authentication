from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    description = models.CharField( max_length=200,)
      
     
    date = models.DateField()
    



    def __str__(self):
        return self.title





from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField("Email address", unique=True)
    age = models.IntegerField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []