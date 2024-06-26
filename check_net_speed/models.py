from django.db import models

# Create your models here.

class UserInternetSpeedData(models.Model):
    email = models.EmailField()
    download_speed = models.FloatField() # Mbps
    upload_speed = models.FloatField() # Mbps
    latency = models.IntegerField() # ms