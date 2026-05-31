from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_pro = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} | PRO={self.is_pro}"

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    set_name = models.CharField(max_length=100)
    current_index = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.set_name} - {self.current_index}"
