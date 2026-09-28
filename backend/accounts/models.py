from django.db import models

from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    display_name = models.CharField(
        max_length=100,
        blank=True
    )

    timezone = models.CharField(
        max_length=50,
        default="Asia/Kolkata"
    )

    proactive_enabled = models.BooleanField(
        default=True
    )

    quiet_hours_start = models.TimeField(
        default="22:00"
    )

    quiet_hours_end = models.TimeField(
        default="07:00"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.user.username