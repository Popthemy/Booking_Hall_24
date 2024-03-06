from django.contrib import admin
from .models import RepProfile

# Register your models here.


@admin.register(RepProfile)
class RepProfileAdmin(admin.ModelAdmin):
    exclude = ['owner',]
    

