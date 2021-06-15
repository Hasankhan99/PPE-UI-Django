from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .views import index,records,Fb,livesteaming,livefe,gallery,deletesnap

urlpatterns = [
    path('', index,name='index'),
    path('Records',records,name='records'),
    path('Fb',Fb,name='Fb'),


    path('livesteaming',livesteaming,name='livesteaming'),
    path('deletesnap/<int:pk>', deletesnap, name='deletesnap'),
    path('livefe/', livefe, name='livefe'),
    path('gallery', gallery, name='gallery'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)