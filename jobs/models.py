from django.db import models

# Create your models here.
class Jobs(models.Model):
    short_name = models.CharField(max_length=50, default='no_project_name')
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    class Meta():
        verbose_name_plural = 'Jobs'
    
    def __str__(self):
        return self.short_name
