from django.utils import timezone

from reminders.models import Reminder

from .proactive import (
    should_nova_speak,
    get_current_routines,
)

from .proactive_messages import (
    build_routine_message,
    build_reminder_message,
)


def get_due_reminder(user):

    now = timezone.now()

    return (
        Reminder.objects
        .filter(
            user=user,
            completed=False,
            remind_at__lte=now,
        )
        .order_by("remind_at")
        .first()
    )


def get_proactive_message(user):

    if not should_nova_speak(user):
        return None

    reminder = get_due_reminder(user)

    if reminder:

        message = build_reminder_message(
            reminder
        )

        reminder.completed = True

        reminder.save(
            update_fields=["completed"]
        )

        return message

    routines = get_current_routines(user)

    if not routines:
        return None

    routine = routines[0]

    return build_routine_message(
        routine
    )