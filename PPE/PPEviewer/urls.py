from django.urls import path 
from .views import index,records,Fb,livesteaming,livefe

urlpatterns = [
    path('', index,name='index'),
    path('Records',records,name='records'),
    path('Fb',Fb,name='Fb'),


    path('livesteaming',livesteaming,name='livesteaming'),
    path('livefe/', livefe, name='livefe'),

]
