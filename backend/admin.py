from django.contrib import admin
from .models import reportModel

# Register your models here.

@admin.register(reportModel)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone','Date','Description','mouvement','user')
