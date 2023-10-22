from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet



# Create your models here.

#------ for preventing from permantly deleted from database---
class ReceipeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)
    

#---DB for Receipes------
class Receipe(models.Model):
    user = models.ForeignKey(User , on_delete= models. SET_NULL , null = True , blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe")
    is_deleted = models.BooleanField(default=False)

    objects = ReceipeManager()
    admin_objects = models.Manager()

