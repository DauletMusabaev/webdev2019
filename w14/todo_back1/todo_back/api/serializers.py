from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TaskList, Task

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        tasklist = TaskList(**validated_data)
        tasklist.save()
        return tasklist
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    task_list_id = serializers.IntegerField(write_only=True)
    # task_list = TaskListSerializer2()

    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status', 'task_list_id')

class TaskSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # task_list = TaskListSerializer2()

    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status',)

class TaskListSerializer2(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    tasks = TaskSerializer2(many=True)
    # tasks = serializers.StringRelatedField(many=True)
    # tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by', 'tasks')

    def create(self, validated_data):
        tasks = validated_data.pop('tasks')
        task_list = TaskList.objects.create(**validated_data)
        for task in tasks:
            Task.objects.create(task_list=task_list, **task)
        # arr = [Task(task_list=task_list, **task) for task in tasks]
        # for i in range(0, len(arr), 100):
        #     # 0 100 200 300
        #     Task.objects.bulk_create(arr[i:i+100])
        return task_list