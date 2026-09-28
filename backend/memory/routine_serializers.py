from rest_framework import serializers

from .models import Routine


class RoutineSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Routine

        fields = [
            "id",
            "routine_type",
            "title",
            "description",
            "usual_time",
            "active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


    def validate_title(
        self,
        value
    ):

        value = value.strip()


        if not value:

            raise serializers.ValidationError(
                "Routine title is required."
            )


        return value