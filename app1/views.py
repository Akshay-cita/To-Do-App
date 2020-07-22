from django.shortcuts import render

# Create your views here
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .models import *
from .serializers import *

@api_view(['GET'])
def TaskList(request):
	tasks=Task.objects.all()
	serializer=TaskSerializer(tasks,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def TaskDetailView(request,pk):
	tasks=Task.objects.get(id=pk)
	serializer=TaskSerializer(tasks,many=False)

	return Response(serializer.data)


@api_view(['POST'])
def TaskCreate(request):
	
	serializer=TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def TaskUpdate(request,pk):
	task=Task.objects.get(id=pk)
	serializer=TaskSerializer(instance=task,data=request.data)

	if serializer.is_valid():
		serializer.save()


	return Response(serializer.data)




@api_view(['DELETE'])
def TaskDelete(request,pk):
	task=Task.objects.get(id=pk)
	task.delete()

	return Response('item successfully deleted!!!')

