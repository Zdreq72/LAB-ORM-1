from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)
    publisher = models.CharField(max_length=256)
    post_image = models.ImageField(upload_to='images/', default='', null=True, blank=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
