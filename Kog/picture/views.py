from django.shortcuts import render
from . import models
# Create your views here.

def dulce(request):
    """
    users = models.User.objects.all()
    for u in users:
        if u.name == 'dulce solter':
            user = u.user_name
    pictures = models.Picture.objects.all()
    pics = []
    for pic in pictures:
         if pic.title == 'dulce solter':
            pics.append(pic)
            """
    users = models.User.objects.all()
    args = {'users': users}
    return render(request, 'dulce/dulce.html', args)
    