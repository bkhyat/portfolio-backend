from django.db import models

# Create your models here.


class NavItems(models.Model):
    name = models.CharField(max_length=50)
