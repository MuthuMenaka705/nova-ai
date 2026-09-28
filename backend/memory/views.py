from rest_framework import viewsets

from rest_framework.permissions import (
    IsAuthenticated,
)

from .models import Memory

from .serializers import (
    MemorySerializer,
)


class MemoryViewSet(viewsets.ModelViewSet):

    serializer_class = (
        MemorySerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return (
            Memory.objects
            .filter(
                user=self.request.user
            )
            .order_by(
                "-importance",
                "-updated_at",
            )
        )

    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            user=self.request.user
        )

    def perform_update(
        self,
        serializer
    ):

        serializer.save(
            user=self.request.user
        )