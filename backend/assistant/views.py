from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated,
)

from .models import Conversation

from .ai_provider import (
    generate_ai_reply,
)

from .emotion import (
    detect_emotion,
)

from .proactive_checker import (
    get_proactive_message,
)

from memory.models import Memory

from memory.services import (
    save_memory_if_needed,
)

from activities.services import (
    save_activity_if_needed,
)


class ChatAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        message = request.data.get(
            "message",
            ""
        ).strip()

        if not message:

            return Response(
                {
                    "error":
                        "Message is required."
                },
                status=400
            )

        try:

            emotion = detect_emotion(
                message
            )

            previous_messages = (
                Conversation.objects
                .filter(
                    user=request.user
                )
                .order_by(
                    "-created_at"
                )[:20]
            )

            previous_messages = list(
                reversed(
                    previous_messages
                )
            )

            conversation_history = [
                {
                    "role": item.role,
                    "message": item.message,
                }
                for item in previous_messages
            ]

            memories = (
                Memory.objects
                .filter(
                    user=request.user,
                    approved=True,
                )
                .order_by(
                    "-importance",
                    "-updated_at",
                )[:20]
            )

            memory_context = [
                {
                    "content": memory.content,
                    "category": memory.category,
                }
                for memory in memories
            ]

            reply = generate_ai_reply(
                message=message,
                conversation_history=
                    conversation_history,
                memory_context=
                    memory_context,
                emotion=emotion,
            )

            Conversation.objects.create(
                user=request.user,
                role="user",
                message=message,
            )

            Conversation.objects.create(
                user=request.user,
                role="assistant",
                message=reply,
            )

            memory = save_memory_if_needed(
                request.user,
                message,
            )

            activity = save_activity_if_needed(
                request.user,
                message,
            )

            return Response({
                "message": message,
                "reply": reply,
                "emotion": emotion,
                "memory_saved":
                    memory is not None,
                "activity_saved":
                    activity is not None,
            })

        except Exception as error:

            print(
                "Nova AI Error:",
                error
            )

            return Response(
                {
                    "error":
                        "Nova could not generate "
                        "a response."
                },
                status=500
            )


class ProactiveCheckAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        message = (
            get_proactive_message(
                request.user
            )
        )

        return Response({
            "should_speak":
                message is not None,
            "message":
                message,
        })