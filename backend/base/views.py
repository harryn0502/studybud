from django.shortcuts import render

rooms = [
  {'id':1, 'name':"Let's learn python!"},
  {'id':2, 'name':"Design with me"},
  {'id':3, 'name':"Frontend developers"},
]


# Create your views here.
def home(request):
  context = {'rooms':rooms}
  return render(request, 'base/home.html', context)

def room(request, id):
  room = None
  for each in rooms:
    if each['id'] == int(id):
      room = each

  context = {'room':room}

  return render(request, 'base/room.html', context)