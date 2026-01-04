from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    likes = models.BigIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    is_public = models.BooleanField(default=False)
