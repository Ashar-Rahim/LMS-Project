from django.contrib.auth.models import AbstractUser
from django.db import models
    
class User(AbstractUser):
    isTeacher = models.BooleanField(default=False)

    def __str__(self):
        return self.username
