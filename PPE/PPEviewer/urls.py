from django.urls import path 
from .views import index,records,Fb,livesteaming

urlpatterns = [
    path('', index,name='index'),
    path('Records',records,name='records'),
    path('Fb',Fb,name='Fb'),
    path('livesteaming',livesteaming,name='livesteaming'),
    

]
