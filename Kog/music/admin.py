from django.contrib import admin
from .models import Music
"""
# Register your models here.
admin.site.register(models.Music)
"""
@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title' , 'slug' , 'published' , 'update']
    search_fields = ['title' , 'slug']
    list_filter = ['title']