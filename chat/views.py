from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ChatRoom(APIView):
    def get(self, request, format=None):
        return Response({'message': 'Hello, World!'})

    def post(self, request, format=None):
        room_number = request.data.get('room_number')
        print(room_number)
        return Response({'room_number': room_number}, status=status.HTTP_201_CREATED)

def index(request):
    return render(request, 'chat/index.html')

def lobby(request, room_name):
    return render(request, 'chat/room.html', {'room_name' : room_name})

def chat_room(request, room_name):
    if request.method == 'POST':
        message = request.POST.get('room_number')
        print(message)
        return HttpResponse({'message': message})