from django.urls import path
from .views import TaskList, TaskDetail



urlpatterns = [
path('<int:pk>/', TaskList.as_view()),
path('', TaskDetail.as_view()),
]