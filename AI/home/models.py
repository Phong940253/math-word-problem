from django.db import models
from django.urls import reverse

# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('home')


