from django.db.models.signals import post_save, pre_save  # noqa
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    """Create a user profile when a user is created.

    This signal is also used for already existing users without a profile.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except UserProfile.DoesNotExist:
            # Create the userprofile if not exist
            UserProfile.objects.create(user=instance)


# @receiver(pre_save, sender=User)
# def pre_save_profile_receiver(sender, instance, **kwargs):
#     pass
# post_save.connect(post_save_create_profile_receiver, sender=User)
