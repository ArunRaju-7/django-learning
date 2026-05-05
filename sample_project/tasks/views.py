from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class CreateTaskView(APIView):
    
    def post(self, request):
        post_serializer = TaskSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListTaskView(APIView):
    
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
class RetrieveTaskView(APIView):
    
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
class UpdateTaskView(APIView):
    
    def post(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteTaskView(APIView):
    
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)