from django.db import models

from django.contrib.auth.models import User


class Reminder(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reminders",
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    remind_at = models.DateTimeField()

    completed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.title