from django.contrib.auth.models import User

from django.db.models.signals import post_save

from django.dispatch import receiver

from .models import UserProfile


@receiver(
    post_save,
    sender=User
)
def create_user_profile(
    sender,
    instance,
    created,
    **kwargs
):

    if created:

        UserProfile.objects.create(
            user=instance,
            display_name=instance.username
        )


@receiver(
    post_save,
    sender=User
)
def save_user_profile(
    sender,
    instance,
    **kwargs
):

    if hasattr(instance, "profile"):

        instance.profile.save(
            update_fields=[
                "updated_at"
            ]
        )