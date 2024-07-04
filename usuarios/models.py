from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class DatosAdicionales(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    avatar =models.ImageField(upload_to='avatares', blank=True, null=True)
    ciudad = models.CharField(max_length=40)


class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
