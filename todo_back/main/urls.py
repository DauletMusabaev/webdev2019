from django.urls import path, re_path
from main import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('time/', views.current_time),
    re_path(r'time/(\d{1,2})/', views.current_time),
    path('products/<int:pk>/', views.show_product)
]