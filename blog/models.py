from django.db import models

# Create your models here.

class Image_Upload(models.Model):
    name_Img = models.ImageField(upload_to='img/')
