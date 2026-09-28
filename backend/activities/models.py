from django.db import models

from django.contrib.auth.models import User


class Activity(models.Model):

    ACTIVITY_TYPES = [

        (
            "work",
            "Work"
        ),

        (
            "study",
            "Study"
        ),

        (
            "food",
            "Food"
        ),

        (
            "exercise",
            "Exercise"
        ),

        (
            "sleep",
            "Sleep"
        ),

        (
            "travel",
            "Travel"
        ),

        (
            "personal",
            "Personal"
        ),

        (
            "other",
            "Other"
        ),
    ]


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="activities",
    )


    activity_type = models.CharField(
        max_length=30,
        choices=ACTIVITY_TYPES,
        default="other",
    )


    description = models.TextField()


    started_at = models.DateTimeField(
        null=True,
        blank=True
    )


    ended_at = models.DateTimeField(
        null=True,
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.description