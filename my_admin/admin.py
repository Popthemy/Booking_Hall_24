from django.contrib import admin
from .models import DefaultRepList

# Register your models here.

@admin.register(DefaultRepList)
class DefualtRepListAdmin(admin.ModelAdmin):
    pass