from ast import Name
import email
from pickle import TRUE
from django.db import models

class table(models.Model):
    name=models.CharField(max_length=255,null=True)
    email=models.EmailField(null=True)
    
