from django.urls import path
from . import views

urlpatterns = [
    path('http://127.0.0.1:8000/', views.post_list, name='post_list'),
]