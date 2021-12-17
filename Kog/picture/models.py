from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=256)
    user_name = models.URLField(max_length=250)

    def __str__(self):
        return self.name


class Picture(models.Model):
    def image_name(instance , filename):
        name = f'picture/{instance.title}.JPG'
        return name

    title = models.CharField(max_length=128)
    slug = models.SlugField()
    image = models.FileField(upload_to= image_name, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='picture')
    publish = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title