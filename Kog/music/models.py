from django.db import models

# Create your models here.
class Music(models.Model):
    def music_name(instance , filename):
        name = f'music/{instance.title} .MP3'
        return name

    title = models.CharField(max_length=256)
    slug = models.SlugField()
    music = models.FileField(upload_to= music_name)
    published = models.DateField(auto_now_add=True, auto_now=False)
    update = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title