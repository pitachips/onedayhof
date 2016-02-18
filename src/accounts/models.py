from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school = models.CharField(max_length=40, null=True)
    major = models.CharField(max_length=40, null=True)
    #phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, **kwargs):
    user =kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(
            user = user,
            school = user.school,
            major = user.major,
            #phone = user.phone,
            )
        user_profile.save()