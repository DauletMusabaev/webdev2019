from django.urls import path
from shop import views

urlpatterns = [
    path('shopper/', views.shopper)
]