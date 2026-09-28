from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = [
        "user",
        "display_name",
        "timezone",
        "proactive_enabled",
        "quiet_hours_start",
        "quiet_hours_end",
    ]

    search_fields = [
        "user__username",
        "display_name",
    ]