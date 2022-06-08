from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serialisers import RoomSerialiser

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
  routes = [
    'GET /api', 
    'GET /api/rooms',
    'GET /api/rooms/:id',
  ]
  return Response(routes)

@api_view(['GET'])
def getRooms(request):
  rooms = Room.objects.all()
  serialiser = RoomSerialiser(rooms, many=True)
  return Response(serialiser.data)

@api_view(['GET'])
def getRoom(request, id):
  rooms = Room.objects.get(id=id)
  serialiser = RoomSerialiser(rooms, many=False)
  return Response(serialiser.data)

# @api_view(['GET'])
# def getNote(request, pk):
#   # param = request.GET.get('id') #Use for (/notes?id=2)
#   note = Note.objects.get(id=pk)
#   serialiser = NoteSerialiser(note, many=False)
#   return Response(serialiser.data)

# @api_view(['POST'])
# def createNote(request):
#   data = request.data
#   note = Note.objects.create(
#     body=data['body']
#   )
#   serialiser = NoteSerialiser(note, many=False)
#   return Response(serialiser.data)

# @api_view(['PUT'])
# def updateNote(request, pk):
#   data = request.data
#   note = Note.objects.get(id=pk)
#   serialiser = NoteSerialiser(instance=note, data=data)
#   if serialiser.is_valid():
#     serialiser.save()

#   return Response(serialiser.data)

# @api_view(['DELETE'])
# def deleteNote(request, pk):
#   note = Note.objects.get(id=pk)
#   note.delete()
#   return Response("Note was deleted!")