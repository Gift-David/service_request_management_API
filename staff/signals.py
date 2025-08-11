from account.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Staff

@receiver(post_save, sender=Staff)
def create_customUser_for_staff(sender, instance, created, **kwargs):
    # create custom user if not exists
    if created and not instance.user:
        user = CustomUser.objects.create(username=instance.username)
        role = CustomUser.objects.create(role=instance.role)
        instance.user = user  
        instance.role = role  
        instance.save()

    # update customuser details if staff is updated
    elif instance.user:
        instance.user.username = instance.username
        instance.user.role = instance.role
        instance.save()