from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User





class Continet(models.Model):
    name = models.CharField(max_length = 255)
    body = RichTextUploadingField (blank = True, null = True)
 
    
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return ('tazelik.html')
    


  