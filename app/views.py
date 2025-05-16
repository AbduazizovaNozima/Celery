from django.http import JsonResponse
from .tasks import sleepy_task
from rest_framework import generics
from . import models
from . import serializers

def run_task(request):
    sleepy_task.delay()  # Orqa fonda 5 soniya uxlaydi
    return JsonResponse({'status': 'Task started in background'})

class UserAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
