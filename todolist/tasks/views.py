from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(assigned_to = user)

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)