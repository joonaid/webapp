from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    site = models.URLField(blank =True)
    imge = models.ImageField(upload_to ='pics', blank =True)
    def __str__(self):
        return self.user.username
