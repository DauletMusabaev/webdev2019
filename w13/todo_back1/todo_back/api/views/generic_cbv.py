from api.models import TaskList
from api.serializers import TaskListSerializer2
from rest_framework import generics

class TaskListMy(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2

    # def get_queryset(self):
    #     return TaskList.objects.all()
    #
    # def get_serializer_class(self):
    #     return TaskListSerializer2

class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2