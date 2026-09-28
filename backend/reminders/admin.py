from django.contrib import admin

from .models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):

    list_display = [
        "user",
        "title",
        "remind_at",
        "completed",
    ]

    list_filter = [
        "completed",
        "remind_at",
    ]

    search_fields = [
        "user__username",
        "title",
        "description",
    ]