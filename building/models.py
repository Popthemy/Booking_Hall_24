from django.db import models
import uuid

# Create your models here.


class Hall(models.Model):

    name = models.CharField(max_length=255)
    hall_image = models.ImageField(
        null=True, blank=True, upload_to='halls/', default='hall.png')
    location = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        """When image get deleted it get no image"""
        try:
            url = self.hall_image.url
        except:
            url = ''
        return url
