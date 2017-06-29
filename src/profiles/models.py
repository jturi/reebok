from __future__ import unicode_literals

from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='default text')
    location = models.CharField(max_length=120, null=True, blank=True)
    job = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.name)