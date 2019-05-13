from django.urls import path
from . import views

# urlpatterns = [
#     path('task_lists/', views.task_list),
#     path('task_lists/<int:pk>/', views.task_list_detail),
#     # path('task_lists/<int:num>/tasks/', views.task_list_num_task)
# ]

urlpatterns = [
    path('task_lists/', views.TaskListMy.as_view()),
    path('task_lists/<int:pk>/', views.TaskListDetail.as_view()),
    path('task_lists/<int:pk>/tasks/', views.TaskListTasks.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views. login),
    path('logout/', views.logout)
]