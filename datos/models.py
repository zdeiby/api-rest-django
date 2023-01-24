from django.db import models

# Create your models here.

class Company(models.Model):
    id=models.AutoField(primary_key=True,
                  serialize = False, 
                  verbose_name ='ID')
    personaje=models.CharField(max_length=50)
    cc=models.CharField(max_length=50)
    celular=models.CharField(max_length=50)

 

