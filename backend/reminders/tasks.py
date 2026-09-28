from celery import shared_task

from django.utils import timezone

from .models import Reminder


@shared_task
def check_due_reminders():

    now = timezone.now()


    reminders = (
        Reminder.objects
        .filter(
            completed=False,
            remind_at__lte=now,
        )
    )


    reminder_data = []


    for reminder in reminders:

        reminder_data.append({

            "id":
                reminder.id,

            "user_id":
                reminder.user_id,

            "title":
                reminder.title,

            "description":
                reminder.description,

            "remind_at":
                reminder.remind_at.isoformat(),

        })


        reminder.completed = True


        reminder.save(
            update_fields=[
                "completed"
            ]
        )


    return reminder_data