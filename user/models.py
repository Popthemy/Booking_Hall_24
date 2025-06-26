from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

import uuid
# Create your models here.

class RepProfile(models.Model):

    MIN_LEVEl, MAX_LEVEL = 100, 800
    LEVELS_CHOICES = [(level, f"{level}L") for level in range(MIN_LEVEl, MAX_LEVEL , 100)]

    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    owner = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    i_am_a_rep = models.BooleanField(default=False)
    level = models.PositiveIntegerField(null=True,blank=True, choices=LEVELS_CHOICES)
    email = models.EmailField(max_length=250)
    contact_info =  PhoneNumberField(null=True, blank=True) # models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def level_display(self):
        for choice in self.LEVELS_CHOICES:
            if choice[0] == self.level:
                return choice[1]
        return '0L'

    class Meta:
        ordering = ['-created']
