from django.urls import path
from .views import RegisterList, RegisterDetail



urlpatterns = [
path('<int:pk>/', RegisterList.as_view()),
path('', RegisterDetail.as_view()),
]
