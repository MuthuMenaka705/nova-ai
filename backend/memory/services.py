import re

from datetime import time

from .models import (
    Memory,
    Routine,
)


MEMORY_KEYWORDS = [

    "i like",
    "i love",
    "i prefer",
    "i usually",
    "i always",
    "i normally",
    "my name is",
    "i work",
    "i study",
    "i live",
    "my routine",
    "every day",
    "daily",
    "usually",
]


def should_save_memory(message):

    text = message.lower().strip()


    return any(
        keyword in text
        for keyword in MEMORY_KEYWORDS
    )


def detect_memory_category(message):

    text = message.lower()


    if any(
        word in text
        for word in [
            "like",
            "love",
            "prefer",
        ]
    ):

        return "preference"


    if any(
        word in text
        for word in [
            "name",
            "live",
        ]
    ):

        return "personal"


    if any(
        word in text
        for word in [
            "work",
            "study",
        ]
    ):

        return "work"


    if any(
        word in text
        for word in [
            "usually",
            "normally",
            "every day",
            "daily",
            "routine",
        ]
    ):

        return "routine"


    return "other"


def save_memory_if_needed(
    user,
    message
):

    if not should_save_memory(message):

        return None


    category = detect_memory_category(
        message
    )


    memory = Memory.objects.create(

        user=user,

        content=message,

        category=category,

        importance=0.7,

        approved=False,
    )


    save_routine_if_needed(
        user,
        message
    )


    return memory


def extract_time(message):

    text = message.lower()


    match = re.search(
        r"\b(\d{1,2})"
        r"(?::(\d{2}))?"
        r"\s*(am|pm)\b",
        text,
    )


    if not match:

        return None


    hour = int(
        match.group(1)
    )


    minute = int(
        match.group(2) or 0
    )


    period = match.group(3)


    if hour > 12:

        return None


    if minute > 59:

        return None


    if period == "pm" and hour != 12:

        hour += 12


    if period == "am" and hour == 12:

        hour = 0


    return time(
        hour=hour,
        minute=minute,
    )


def detect_routine_type(message):

    text = message.lower()


    if any(
        word in text
        for word in [
            "lunch",
            "breakfast",
            "dinner",
            "eat",
            "food",
            "sapdu",
            "sapten",
            "saptiya",
        ]
    ):

        return "meal"


    if any(
        word in text
        for word in [
            "work",
            "office",
            "job",
        ]
    ):

        return "work"


    if any(
        word in text
        for word in [
            "study",
            "college",
            "class",
        ]
    ):

        return "study"


    if any(
        word in text
        for word in [
            "sleep",
            "bed",
            "thoongu",
            "thoonguren",
        ]
    ):

        return "sleep"


    if any(
        word in text
        for word in [
            "exercise",
            "gym",
            "workout",
        ]
    ):

        return "exercise"


    return "other"


def save_routine_if_needed(
    user,
    message
):

    text = message.lower()


    routine_words = [

        "usually",
        "normally",
        "every day",
        "daily",
        "always",
    ]


    has_routine_word = any(
        word in text
        for word in routine_words
    )


    if not has_routine_word:

        return None


    routine_time = extract_time(
        message
    )


    routine_type = detect_routine_type(
        message
    )


    routine, created = (
        Routine.objects.update_or_create(

            user=user,

            title=message[:200],

            defaults={

                "routine_type":
                    routine_type,

                "description":
                    message,

                "usual_time":
                    routine_time,

                "active":
                    True,
            },
        )
    )


    return routine