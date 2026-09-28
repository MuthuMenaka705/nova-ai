from datetime import datetime

from accounts.models import UserProfile

from memory.models import Routine


def is_quiet_hours(
    current_time,
    start_time,
    end_time
):

    if start_time < end_time:

        return (
            start_time
            <= current_time
            < end_time
        )

    return (
        current_time >= start_time
        or current_time < end_time
    )


def should_nova_speak(user):

    try:

        profile = user.profile

    except UserProfile.DoesNotExist:

        return False


    if not profile.proactive_enabled:

        return False


    current_time = datetime.now().time()


    if is_quiet_hours(
        current_time,
        profile.quiet_hours_start,
        profile.quiet_hours_end,
    ):

        return False


    return True


def get_current_routines(user):

    current_time = datetime.now().time()


    routines = (
        Routine.objects
        .filter(
            user=user,
            active=True,
            usual_time__isnull=False,
        )
        .order_by("usual_time")
    )


    nearby_routines = []


    current_minutes = (
        current_time.hour * 60
        + current_time.minute
    )


    for routine in routines:

        routine_minutes = (
            routine.usual_time.hour * 60
            + routine.usual_time.minute
        )


        difference = abs(
            routine_minutes
            - current_minutes
        )


        if difference <= 30:

            nearby_routines.append(
                routine
            )


    return nearby_routines