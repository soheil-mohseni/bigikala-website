from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#  user = models.ForeignKey (User,on_delete=models.CASCADE)

    
class product(models.Model):
    name= models.CharField(max_length= 30)
    price= models.IntegerField(default=0)
    def __str__(self):
        return f'{self.name}'

class basket(models.Model):
    metal= models.CharField(max_length= 30)
    money= models.IntegerField(default=0)
    user = models.ForeignKey (User,on_delete=models.CASCADE)
    
