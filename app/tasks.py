from celery import shared_task
import random
from . import models


@shared_task
def sleepy_task():
    print("⏰ Har 5 sekundda ishlovchi task ishga tushdi!")
    return "Task executed"


@shared_task
def update_user_age_every_5_seconds():
    users = models.User.objects.all()
    for user in users:
        new_age = str(random.randint(18, 50))
        user.age = new_age
        user.save()
        print(f"{user.name} uchun yosh yangilandi: {new_age}")
    return "Barcha foydalanuvchilarning yoshi yangilandi."




