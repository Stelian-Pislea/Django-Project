from django.urls import path
from . import views

app_name = 'my_site'

urlpatterns = [
    path('homepage/', views.home_page, name='homepage'),
    path('pc/', views.pc, name='pc'),
    path('playstation/', views.playstation, name='playstation'),

    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]

