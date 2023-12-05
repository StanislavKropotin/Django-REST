from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.decorators import login_required

from .models import *
from .serializers import *


# Create your views here.
def rooms(request):
    rooms = Room.objects.all()
    return render(request, "rooms.html", {'rooms': rooms})

def room(request, slug):
    room_name = Room.objects.get(slug=slug).name
    messages = Message.objects.filter(room=Room.objects.get(slug=slug))
    users = User.objects.filter(message__room=Room.objects.get(slug=slug)).distinct()
    context = {
        "slug": slug,
        "room_name": room_name,
        "messages":messages,
        "users":users,
        }
    return render(request, "room.html", context)


class RoomAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# class UserAPIView(generics.ListAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserSerializer


@login_required
def profile_view (request):
    return render(request, "profile.html")


