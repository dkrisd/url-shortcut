from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=100)
    url_shortcut = models.CharField(max_length=20)