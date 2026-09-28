from django.contrib import admin

from .models import (
    Memory,
    Routine,
)


@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):

    list_display = [
        "user",
        "category",
        "importance",
        "approved",
        "created_at",
    ]

    list_filter = [
        "category",
        "approved",
    ]

    search_fields = [
        "user__username",
        "content",
    ]


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):

    list_display = [
        "user",
        "routine_type",
        "title",
        "usual_time",
        "active",
    ]

    list_filter = [
        "routine_type",
        "active",
    ]

    search_fields = [
        "user__username",
        "title",
    ]