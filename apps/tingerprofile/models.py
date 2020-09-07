from django.db import models
from django.contrib.auth.models import User

class TingerProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
  avatar = models.ImageField(upload_to='uploads/', blank=True, null=True)

User.tingerprofile = property(lambda  u:TingerProfile.objects.get_or_create(user=u)[0])