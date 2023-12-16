from django.urls import path
from Myapp import views
from .views import index#, BA, SUM
# from .views import get_json_data

urlpatterns = [
    #path('', views.index, name='index'),
    #path('Bluearchive/', views.BA),
    #path('Maplestroy/', views.MS),
    #path('Main/', views.main)

    #path('',views.main, name='index')
    path('', index, name='index'),
    #path('Bluearchive/', BA, name='BA'),
    #path('Summary/', SUM, name='SUM'),
    #(', views.json, name='get_json_data') 12/04 추가
    #path('get_json_data/', get_json_data, name='get_json_data'),
]
