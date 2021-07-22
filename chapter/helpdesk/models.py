from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=264)   
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=500)  


