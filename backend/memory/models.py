from django.db import models

from django.contrib.auth.models import User


class Memory(models.Model):

    CATEGORY_CHOICES = [

        (
            "preference",
            "Preference"
        ),

        (
            "personal",
            "Personal"
        ),

        (
            "work",
            "Work"
        ),

        (
            "routine",
            "Routine"
        ),

        (
            "other",
            "Other"
        ),
    ]


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="memories",
    )


    content = models.TextField()


    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="other",
    )


    importance = models.FloatField(
        default=0.5
    )


    approved = models.BooleanField(
        default=False
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):

        return self.content


class Routine(models.Model):

    ROUTINE_TYPES = [

        (
            "meal",
            "Meal"
        ),

        (
            "work",
            "Work"
        ),

        (
            "study",
            "Study"
        ),

        (
            "sleep",
            "Sleep"
        ),

        (
            "exercise",
            "Exercise"
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
        related_name="routines",
    )


    routine_type = models.CharField(
        max_length=30,
        choices=ROUTINE_TYPES,
        default="other",
    )


    title = models.CharField(
        max_length=200
    )


    description = models.TextField(
        blank=True
    )


    usual_time = models.TimeField(
        null=True,
        blank=True
    )


    active = models.BooleanField(
        default=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):

        return self.title