from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)

    # when an object is printed, it transforms the object into human readable format
    def __str__(self):
        return self.title



