from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Room

rooms = [
    {'id':1, 'name':'Python'},
    {'id':2, 'name':'Java'},
    {'id':3, 'name':'JavaScript'},
]

def home(request):
    rooms = Room.objects.all()
    
    context = {'rooms':rooms}
    # return HttpResponse("Home Page")
    return render(request, 'base/home.html', context)

def room(request,pk):
    # room = None
    room = Room.objects.get(id=pk)
    # for i in rooms:
    #     if i['id']==int(pk):
    #         print(i)
    #         room=i
    context = {'room':room}
    # return HttpResponse("Room Page")
    return render(request, 'base/room.html',context)

