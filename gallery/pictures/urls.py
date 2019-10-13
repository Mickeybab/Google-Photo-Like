from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-album/', views.add_album, name='add_album'),
    path('upload', views.upload, name='upload'),
    path('album', views.album, name='album'),
    path('album/<int:id>', views.see_album, name="see album")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)