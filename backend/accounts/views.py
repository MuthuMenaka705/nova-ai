from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from .models import UserProfile

from .serializers import UserProfileSerializer


class UserProfileAPIView(
    generics.RetrieveUpdateAPIView
):

    serializer_class = (
        UserProfileSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    def get_object(self):

        profile, created = (
            UserProfile.objects.get_or_create(
                user=self.request.user,

                defaults={
                    "display_name":
                        self.request.user.username,
                }
            )
        )

        return profile