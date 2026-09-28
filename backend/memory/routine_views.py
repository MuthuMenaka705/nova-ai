from rest_framework import viewsets

from rest_framework.permissions import (
    IsAuthenticated,
)

from .models import Routine

from .routine_serializers import (
    RoutineSerializer,
)


class RoutineViewSet(
    viewsets.ModelViewSet
):

    serializer_class = (
        RoutineSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]


    def get_queryset(self):

        return (
            Routine.objects
            .filter(
                user=self.request.user
            )
            .order_by(
                "usual_time"
            )
        )


    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            user=self.request.user
        )