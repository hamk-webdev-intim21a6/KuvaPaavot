from enum import unique
from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, null=True,  on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)




    # settings.AUTH_USER_MODEL