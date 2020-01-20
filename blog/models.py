from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/images/', blank=True)

    class Meta():
        verbose_name_plural = 'Blog'
    
    def __str__(self):
        return self.title + " " + str(self.published_date)
