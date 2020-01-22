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
        return self.title + " " + self.published_date.strftime('%b %e %Y')

    def body_summary(self):
        return self.body[:100] + " ..."
    
    def published_date_formatted(self):
        return self.published_date.strftime('%b %e %Y')