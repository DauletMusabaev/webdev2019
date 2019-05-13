from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, UserSerializer, TaskSerializer
from api.filters import TaskFilter

# class TaskListMy(generics.ListAPIView):
#     queryset = TaskList.objects.all()
#     serializer_class = TaskListSerializer2
#     http_method_names = ['get',]


class TaskListMy(generics.ListCreateAPIView):
    # queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2
    # http_method_names = ['get',]
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    # def get_serializer_class(self):
    #     return TaskListSerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2

class TaskListTasks(generics.ListCreateAPIView):

    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    # TODO DjangoFilterBackend
    filter_class = TaskFilter

    # TODO SearchFilter
    search_fields = ('name', 'id')

    # TODO OrderingFilter
    ordering_fields = ('name', 'id')

    ordering = ('name', )

    def get_queryset(self):
        try:
            task_list = TaskList.objects.get(id=self.kwargs.get('pk'))
        except TaskList.DoesNotExist as e:
            return Http404
        tasks = task_list.tasks.all()
        return tasks