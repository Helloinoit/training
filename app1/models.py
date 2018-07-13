import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Photo(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to="gallery")
    photo_text = models.CharField(max_length=160)

    def __str__(self):
        return self.photo_text

    def show_photo(self):
        return self.photo





