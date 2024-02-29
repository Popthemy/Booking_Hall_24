from django.contrib import admin
from .models import RepProfile,DefaultRepList

# Register your models here.


@admin.register(DefaultRepList)
class DefualtRepListAdmin(admin.ModelAdmin):
    pass

@admin.register(RepProfile)
class RepProfileAdmin(admin.ModelAdmin):
    exclude = ['owner',]
    

