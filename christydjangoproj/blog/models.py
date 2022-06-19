from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class blogpost(models.Model):
    title   =models.CharField(max_length=200)
    body    =models.TextField(max_length=5000, null=False, blank=False)
    Author  =models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date =models.DateTimeField(auto_now=True, verbose_name='date_created')
    Published_date =models.DateTimeField(auto_now_add=True, verbose_name='date_published')

