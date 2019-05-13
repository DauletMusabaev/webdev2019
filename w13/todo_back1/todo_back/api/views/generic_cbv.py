from api.models import TaskList
from api.serializers import TaskListSerializer2, UserSerializer, TaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
# from rest_framework.filters import


# class TaskListMy(generics.ListAPIView):
#     queryset = TaskList.objects.all()
#     serializer_class = TaskListSerializer2
#     http_method_names = ['get',]


class TaskListMy(generics.ListCreateAPIView):
    # queryset = TaskList.objects.all()
    # serializer_class = TaskListSerializer2
    # http_method_names = ['get',]
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2

class TaskListTasks(generics.ListAPIView):
    def get_queryset(self):
        try:
            task_list = TaskList.objects.get(id=self.kwargs.get('pk'))
        except:
            return Http404
        tasks = task_list.task_set.all()
        return tasks
    serializer_class = TaskSerializer