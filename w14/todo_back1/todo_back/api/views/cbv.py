from api.models import TaskList
from api.serializers import TaskListSerializer2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class TaskListMy(APIView):
    def get(self, request):
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer2(task_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TaskListDetail(APIView):
    def get_object(self, pk):
        try:
            return True, TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        found, task_list = self.get_object(pk)
        if found:
            serializer = TaskListSerializer2(task_list)
            return Response(serializer.data)
        return task_list
    def put(self, request, pk):
        found, task_list = self.get_object(pk)
        serializer = TaskListSerializer2(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, pk):
        found, task_list = self.get_object(pk)
        task_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)