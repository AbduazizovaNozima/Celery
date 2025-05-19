from django.urls import path
from .views import run_task, UserAPIView

urlpatterns = [
    path('run-task/', run_task, name='run-task'),
    path('user/', UserAPIView.as_view()),
]


