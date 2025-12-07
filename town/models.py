from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class User(AbstractUser):
    ...
    

class House(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    svg_content = models.TextField(blank=True, null=True)
    owner = models.OneToOneField('town.User', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)