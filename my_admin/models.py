from django.db import models
from user.models import RepProfile
# Create your models here.
import uuid
# Create your models here.

class DefaultRepList(models.Model):

    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    admin = models.ForeignKey(RepProfile, null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=250)


    def __str__(self):
        return self.first_name + self.last_name
