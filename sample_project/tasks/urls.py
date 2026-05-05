from django.urls import path
from .views import CreateTaskView, ListTaskView, RetrieveTaskView, UpdateTaskView, DeleteTaskView

urlpatterns = [
    path('tasks/', ListTaskView.as_view(), name='task-list'),
    path('tasks/create/', CreateTaskView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', RetrieveTaskView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', UpdateTaskView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', DeleteTaskView.as_view(), name='task-delete'),
]