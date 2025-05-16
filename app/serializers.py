from rest_framework import serializers
from rest_framework.validators import ValidationError
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('name', "age", "phone")


