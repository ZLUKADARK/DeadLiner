from rest_framework.decorators import api_view
from rest_framework import status, permissions, generics
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from .serializers import TaskSerializer, ListSerializer
from .models import Task
"""
API Overview
"""
class ViewPermission(generics.ListAPIView):
    queryset = Task.objects.all()
    task = Task.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated] 
  

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
        'Create.User' : '/api/v1/auth/',
        'login.User' : '/api/v1/auth/user/user/by/token/',

    }
    return Response(api_urls)

class taskList(ViewPermission):
    # @api_view(['GET'])
    def taskList(request):
        tasks = Task.objects.all()
        serializer = ListSerializer(tasks, many = True)
        return Response(serializer.data)
            



class taskDetail(ViewPermission):
    @api_view(['GET'])
    def taskDetail(request, pk):
        try:
            tasks = Task.objects.get(id=pk)
            serializer = TaskSerializer(tasks, many = False)
            return Response(serializer.data)
        except Task.DoesNotExist:
                return Response(status=status.HTTP_204_NO_CONTENT)

class taskUpdate(ViewPermission):
    @api_view(['POST'])
    def taskUpdate(request, pk):
        task = Task.objects.get(id = pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class taskCreate(ViewPermission):
    @api_view(['POST'])
    def taskCreate(request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class taskDelete(ViewPermission):
    @api_view(['DELETE'])
    def taskDelete(request, pk):
        try:
            task = Task.objects.get(id = pk)
            task.delete()
            return Response("Task deleted successfully.")
        except Task.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

 