from .models import Activity


ACTIVITY_KEYWORDS = {

    "work": [
        "went to work",
        "going to work",
        "at work",
        "finished work",
        "work finished",
        "office",
    ],

    "study": [
        "studying",
        "study",
        "college",
        "class",
    ],

    "food": [
        "ate",
        "eating",
        "had lunch",
        "had dinner",
        "had breakfast",
        "sapten",
        "saptiya",
        "lunch",
        "dinner",
        "breakfast",
    ],

    "exercise": [
        "gym",
        "workout",
        "exercising",
        "exercise",
    ],

    "sleep": [
        "sleeping",
        "slept",
        "going to sleep",
        "thoonguren",
    ],

    "travel": [
        "travelling",
        "traveling",
        "came back",
        "returned",
    ],
}


def detect_activity_type(
    message
):

    text = message.lower()


    for (
        activity_type,
        keywords
    ) in ACTIVITY_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:

                return activity_type


    return None


def save_activity_if_needed(
    user,
    message
):

    activity_type = (
        detect_activity_type(
            message
        )
    )


    if not activity_type:

        return None


    return Activity.objects.create(

        user=user,

        activity_type=activity_type,

        description=message,
    )