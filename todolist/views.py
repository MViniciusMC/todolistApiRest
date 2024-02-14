from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer


    
class TaskListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Lista apenas as tarefas associadas ao usuário autenticado
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Cria uma nova tarefa associada ao usuário autenticado
        data = {'user': request.user.id, 'name': request.data.get('name'), 'done': False}
        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
