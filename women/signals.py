from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from women.models import Women


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Women.objects.create(user=instance)
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.women.save()
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
