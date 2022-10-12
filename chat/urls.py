from django.urls import path
from chat import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/', views.ChatRoom.as_view(), name='room'),
    path('<str:room_name>/', views.chat_room, name='room')
]