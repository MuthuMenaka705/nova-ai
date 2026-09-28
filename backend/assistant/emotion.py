def detect_emotion(message):
    text = message.lower().strip()

    if any(word in text for word in [
        "happy",
        "great",
        "awesome",
        "super",
        "love",
        "excited",
        "semma",
        "mass",
    ]):
        return "happy"

    if any(word in text for word in [
        "sad",
        "depressed",
        "upset",
        "cry",
        "hurt",
        "feel bad",
        "kastama",
        "kashtama",
    ]):
        return "sad"

    if any(word in text for word in [
        "angry",
        "mad",
        "frustrated",
        "irritated",
        "kovam",
    ]):
        return "angry"

    if any(word in text for word in [
        "tired",
        "exhausted",
        "sleepy",
        "sorvu",
        "tired ah",
    ]):
        return "tired"

    if any(word in text for word in [
        "worried",
        "anxious",
        "scared",
        "tension",
        "bayama",
        "worry",
    ]):
        return "worried"

    return "neutral"