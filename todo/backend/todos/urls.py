from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view(), name='detail-todo'),
    path('', ListTodo.as_view(), name='list-todo'),
]