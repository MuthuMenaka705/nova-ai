from django.contrib import admin

from .models import Conversation


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):

    list_display = [
        "user",
        "role",
        "created_at",
    ]

    list_filter = [
        "role",
        "created_at",
    ]

    search_fields = [
        "user__username",
        "message",
    ]