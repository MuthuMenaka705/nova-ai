from rest_framework import serializers

from .models import Activity


class ActivitySerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Activity

        fields = [
            "id",
            "activity_type",
            "description",
            "started_at",
            "ended_at",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]


    def validate_description(
        self,
        value
    ):

        value = value.strip()


        if not value:

            raise serializers.ValidationError(
                "Activity description is required."
            )


        return value