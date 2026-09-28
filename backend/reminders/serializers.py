from rest_framework import serializers

from .models import Reminder


class ReminderSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Reminder

        fields = [
            "id",
            "title",
            "description",
            "remind_at",
            "completed",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]


    def validate_title(
        self,
        value
    ):

        value = value.strip()


        if not value:

            raise serializers.ValidationError(
                "Reminder title is required."
            )


        return value