from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Room
from .forms import RoomForm

# rooms = [
#     {'id':1, 'name':'Python'},
#     {'id':2, 'name':'Java'},
#     {'id':3, 'name':'JavaScript'},
# ]

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

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request, 'base/room_form.html',context)


