from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True,null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    pincode= models.IntegerField(max_length=6, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class UploadCattleImage(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True,null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    pincode= models.IntegerField(max_length=6, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)