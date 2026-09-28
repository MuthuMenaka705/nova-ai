def build_routine_message(routine):

    if routine.routine_type == "meal":

        return (
            f"Hey, it's around "
            f"{routine.title} time. "
            f"Have you eaten?"
        )


    if routine.routine_type == "work":

        return (
            f"Hey, it's around "
            f"{routine.title} time. "
            f"Ready for work?"
        )


    if routine.routine_type == "study":

        return (
            f"Hey, it's around "
            f"{routine.title} time. "
            f"Ready to study?"
        )


    if routine.routine_type == "exercise":

        return (
            f"Hey, it's around "
            f"{routine.title} time. "
            f"Time for a workout?"
        )


    if routine.routine_type == "sleep":

        return (
            f"Hey, it's around "
            f"{routine.title} time. "
            f"Getting ready to sleep?"
        )


    return (
        f"Hey, it's around "
        f"{routine.title} time."
    )


def build_reminder_message(reminder):

    return (
        f"Reminder: {reminder.title}."
    )