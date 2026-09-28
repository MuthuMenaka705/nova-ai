from django.contrib import admin

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from assistant.views import (
    ChatAPIView,
    ProactiveCheckAPIView,
)

from accounts.views import (
    UserProfileAPIView,
)

from memory.views import (
    MemoryViewSet,
)

from memory.routine_views import (
    RoutineViewSet,
)

from reminders.views import (
    ReminderViewSet,
)

from activities.views import (
    ActivityViewSet,
)


router = DefaultRouter()


router.register(
    r"memories",
    MemoryViewSet,
    basename="memory"
)


router.register(
    r"routines",
    RoutineViewSet,
    basename="routine"
)


router.register(
    r"reminders",
    ReminderViewSet,
    basename="reminder"
)


router.register(
    r"activities",
    ActivityViewSet,
    basename="activity"
)


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "api/auth/login/",
        TokenObtainPairView.as_view(),
        name="login"
    ),

    path(
        "api/auth/refresh/",
        TokenRefreshView.as_view(),
        name="refresh"
    ),

    path(
        "api/chat/",
        ChatAPIView.as_view(),
        name="chat"
    ),

    path(
        "api/profile/",
        UserProfileAPIView.as_view(),
        name="profile"
    ),

    path(
        "api/proactive/check/",
        ProactiveCheckAPIView.as_view(),
        name="proactive-check"
    ),

    path(
        "api/",
        include(router.urls)
    ),
]