from django.db import models
from django.contrib.auth.models import User

class Ting(models.Model):
  body = models.CharField(max_length=255)

  created_by = models.ForeignKey(User, related_name='tings', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'Ting'
    verbose_name_plural = 'Tings'
    ordering = ('-modified_at',)