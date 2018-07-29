from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete='')
    email = models.CharField(max_length=64)
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

def createProfile(sender, **kwargs):
    if kwargs['created']:
        userProfile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(createProfile, sender=User)