from django.db import models
import uuid
from cloudinary.models import CloudinaryField

# Create your models here.


class Hall(models.Model):
    DEFAULT_HALL_IMAGE = 'https://res.cloudinary.com/dtbf1jnph/image/upload/v1709344440/halls/z72wqp7xmshse2nrxbzk.png'

    name = models.CharField(max_length=255)
    # hall_image = models.ImageField( 
        # null=True, blank=True, upload_to='halls/', default='dz2xsylz9dzakdpupstd') #default hall.png
    hall_image = CloudinaryField(default=DEFAULT_HALL_IMAGE , folder='halls/' , null=True, blank=True)

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
    
    def save(self, *args, **kwargs):
        if self.hall_image:
            self.hall_image.options = {"quality": "auto"}
        super().save(*args, **kwargs)
