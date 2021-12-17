from django.contrib import admin
from .models import Picture , User

# Register your models here.
@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['title', 'user','publish']
    

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass