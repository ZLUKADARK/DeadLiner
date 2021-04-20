from rest_framework.decorators import api_view
from rest_framework import status, permissions, generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from .serializers import TaskSerializer, ListSerializer
from .models import Task

"""
API Overview
"""



class ViewListPermission(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]



class ViewPermission(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]




@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
        'Create.User' : '/api/register/',
        'login.User' : '/api/login/',
        'logout.User' : '/api/logout/',
        'logoutall.User' : '/api/logoutall/',

    }
    return Response(api_urls)

class taskList(ViewListPermission):
    @api_view(['GET'])
    def taskList(request):
        tasks = Task.objects.all()
        serializer = ListSerializer(tasks, many = True)
        return  Response(serializer.data)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
        
            
class taskDetail(ViewPermission):
    @api_view(['GET'])
    def taskDetail(request, pk):
        try:
            tasks = Task.objects.get(id = pk)
            serializer = TaskSerializer(tasks, many = False)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

class taskUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated] 
    @api_view(['POST'])
    def taskUpdate(request, pk):
        task = Task.objects.get(id = pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class taskCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    @api_view(['POST'])
    def taskCreate(request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class taskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated] 
    @api_view(['DELETE'])
    def taskDelete(request, pk):
        try:
            task = Task.objects.get(id = pk)
            task.delete()
            return Response("Task deleted successfully.")
        except Task.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)


 