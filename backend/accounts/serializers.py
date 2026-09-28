from rest_framework import serializers

from .models import UserProfile


class UserProfileSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = UserProfile

        fields = [
            "display_name",
            "timezone",
            "proactive_enabled",
            "quiet_hours_start",
            "quiet_hours_end",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
        ]