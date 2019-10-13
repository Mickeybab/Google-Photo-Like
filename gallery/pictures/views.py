import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from pictures.models import Album

# Create your views here.
def index(request):
    path = settings.MEDIA_ROOT
    alb_list = os.listdir(path)
    result = []
    for alb in alb_list:
        for image in os.listdir(os.path.join(path, alb)):
            result.append(os.path.join(alb, image))
    context = {'images' : result}
    return render(request, "pictures/index.html", context)

def add_album(request):
    if request.method == 'POST' and request.POST['title'] and request.POST['description'] and request.FILES['cover']:
        name = request.POST['title']
        description = request.POST['description']
        cover = request.FILES['cover']
        path = os.path.join(settings.MEDIA_ROOT, name)
        album = Album(title=name, description=description, path=path, cover=cover.name)
        album.save()
        os.mkdir(path)
        fs = FileSystemStorage()
        file_name_path = os.path.join(name, cover.name)
        filename = fs.save(file_name_path, cover)
        fs.url(filename)
    return render(request, "pictures/add_album.html")

def upload(request):
    all_album = Album.objects.all()
    albums_names = []
    for album in all_album:
        albums_names.append(str(album.title))
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(os.path.join(request.POST['album'], myfile.name), myfile)
        uploaded_file_url = fs.url(filename)
    context = {'albums': albums_names}
    return render(request, "pictures/upload.html", context)

def album(request):
    albums = Album.objects.all()
    result = []
    for album in albums:
        album.cover = os.path.join(album.title, album.cover)
        result.append(album)
    context = {'albums': result}
    return render(request, "pictures/album.html", context)

def see_album(request, id=0):
    albums = Album.objects.all()
    name = ''
    result = []
    for album in albums:
        if album.id == id:
            name = album.title
    for img in os.listdir(os.path.join(settings.MEDIA_ROOT, name)):
        result.append(os.path.join(name, img))
    context = {'images': result, 'name': name}
    return render(request, "pictures/see_album.html", context)