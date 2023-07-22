from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    def __str__(self):
        return self.email

class Label(models.Model):
    User = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE, default="")
    data = models.TextField(default='{"labeles": [], "values": []}')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.User.email

    class Meta:
        ordering = ['-create_time']
        verbose_name = 'Label TB'
        verbose_name_plural = 'Labels TB'

@receiver(post_save, sender=User)
def create_monster_table(sender, instance, created, **kwargs):
    if created:
        print("New user created!")
        Label.objects.create(User=instance)