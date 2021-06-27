from django.db import models

class log(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    username=models.CharField(max_length=200,null=True,blank=True)
    password = models.CharField(max_length=200,null=True,blank=True)
    upload = models.FileField(upload_to='uploads/',null=True,blank=True)
