import {
    useEffect,
    useRef,
    useState,
} from "react";

import api from "../services/api";


function VoiceAssistant({
    onLogout,
    onOpenProfile,
    onOpenReminders,
}) {

    const [message, setMessage] =
        useState("");

    const [reply, setReply] =
        useState("");

    const [listening, setListening] =
        useState(false);

    const [thinking, setThinking] =
        useState(false);

    const [proactiveEnabled, setProactiveEnabled] =
        useState(false);

    const recognitionRef =
        useRef(null);

    const proactiveTimerRef =
        useRef(null);


    const speak = (text) => {

        if (!window.speechSynthesis) {
            return;
        }

        window.speechSynthesis.cancel();

        const speech =
            new SpeechSynthesisUtterance(text);

        speech.lang = "en-US";
        speech.rate = 0.95;
        speech.pitch = 1;

        window.speechSynthesis.speak(
            speech
        );
    };


    const sendMessage = async (text) => {

        const cleanText =
            text.trim();

        if (!cleanText) {
            return;
        }

        try {

            setThinking(true);

            const response =
                await api.post(
                    "/chat/",
                    {
                        message:
                            cleanText,
                    }
                );

            const aiReply =
                response.data.reply;

            setReply(aiReply);

            speak(aiReply);

        } catch (error) {

            console.error(error);

            setReply(
                "Sorry, I couldn't connect to Nova."
            );

        } finally {

            setThinking(false);
        }
    };


    const startListening = () => {

        const SpeechRecognition =
            window.SpeechRecognition ||
            window.webkitSpeechRecognition;

        if (!SpeechRecognition) {

            alert(
                "Please use Google Chrome for voice input."
            );

            return;
        }

        if (listening) {
            return;
        }

        const recognition =
            new SpeechRecognition();

        recognition.lang =
            "en-US";

        recognition.continuous =
            false;

        recognition.interimResults =
            false;


        recognition.onstart = () => {

            setListening(true);
        };


        recognition.onend = () => {

            setListening(false);
        };


        recognition.onerror = (
            event
        ) => {

            console.error(
                "Speech recognition error:",
                event
            );

            setListening(false);
        };


        recognition.onresult = (
            event
        ) => {

            const text =
                event.results[0][0]
                    .transcript;

            setMessage(text);

            sendMessage(text);
        };


        recognitionRef.current =
            recognition;

        recognition.start();
    };


    const stopListening = () => {

        if (
            recognitionRef.current
        ) {

            recognitionRef.current.stop();

            recognitionRef.current =
                null;
        }

        setListening(false);
    };


    const handleSubmit = (
        event
    ) => {

        event.preventDefault();

        sendMessage(message);
    };


    const checkProactiveMessage =
        async () => {

            try {

                const response =
                    await api.get(
                        "/proactive/check/"
                    );

                if (
                    response.data
                        .should_speak &&
                    response.data.message
                ) {

                    const proactiveMessage =
                        response.data.message;

                    setReply(
                        proactiveMessage
                    );

                    speak(
                        proactiveMessage
                    );
                }

            } catch (error) {

                console.error(
                    "Proactive check failed:",
                    error
                );
            }
        };


    useEffect(() => {

        const loadProfile =
            async () => {

                try {

                    const response =
                        await api.get(
                            "/profile/"
                        );

                    setProactiveEnabled(
                        response.data
                            .proactive_enabled
                    );

                } catch (error) {

                    console.error(error);
                }
            };


        loadProfile();

    }, []);


    useEffect(() => {

        if (!proactiveEnabled) {

            return;
        }

        checkProactiveMessage();

        proactiveTimerRef.current =
            setInterval(
                checkProactiveMessage,
                60000
            );


        return () => {

            if (
                proactiveTimerRef.current
            ) {

                clearInterval(
                    proactiveTimerRef.current
                );

                proactiveTimerRef.current =
                    null;
            }
        };

    }, [proactiveEnabled]);


    return (
        <div className="assistant-page">

            <header className="assistant-header">

                <div className="brand">

                    <div className="brand-orb">
                        ✦
                    </div>

                    <div>

                        <div className="brand-name">
                            NOVA
                        </div>

                        <div className="brand-status">
                            Personal AI
                        </div>

                    </div>

                </div>


                <div className="header-actions">

                    <button
                        className="header-button"
                        onClick={
                            onOpenReminders
                        }
                    >
                        Reminders
                    </button>


                    <button
                        className="header-button"
                        onClick={
                            onOpenProfile
                        }
                    >
                        Settings
                    </button>


                    <button
                        className="logout-button"
                        onClick={onLogout}
                    >
                        Logout
                    </button>

                </div>

            </header>


            <main className="assistant-main">

                <section className="hero-section">

                    <div className="status-pill">

                        <span className="status-dot"></span>

                        {thinking
                            ? "Nova is thinking..."
                            : listening
                                ? "Listening..."
                                : "Nova is ready"
                        }

                    </div>


                    <h1>

                        What can I do
                        <br />

                        <span>
                            for you?
                        </span>

                    </h1>


                    <p>

                        Ask anything, start a conversation,
                        <br />

                        or simply talk to Nova.

                    </p>

                </section>


                <div
                    className={
                        `nova-core ${
                            listening
                                ? "active"
                                : ""
                        } ${
                            thinking
                                ? "thinking"
                                : ""
                        }`
                    }
                >

                    <div className="core-ring ring-one"></div>

                    <div className="core-ring ring-two"></div>

                    <div className="core-glow"></div>

                    <div className="core-symbol">
                        ✦
                    </div>

                </div>


                <button
                    className={
                        `voice-button ${
                            listening
                                ? "listening"
                                : ""
                        }`
                    }
                    onClick={
                        listening
                            ? stopListening
                            : startListening
                    }
                >

                    <span className="mic-icon">

                        {listening
                            ? "●"
                            : "🎙"
                        }

                    </span>


                    <span>

                        {listening
                            ? "Stop listening"
                            : "Talk to Nova"
                        }

                    </span>

                </button>


                <section className="input-section">

                    <form
                        className="message-box"
                        onSubmit={
                            handleSubmit
                        }
                    >

                        <span className="input-icon">
                            ✦
                        </span>


                        <input
                            type="text"
                            value={message}
                            placeholder="Ask Nova anything..."
                            onChange={(event) =>
                                setMessage(
                                    event.target.value
                                )
                            }
                        />


                        <button
                            type="submit"
                            className="send-button"
                            disabled={
                                !message.trim() ||
                                thinking
                            }
                        >
                            →
                        </button>

                    </form>

                </section>


                {reply && (

                    <section className="response-card">

                        <div className="response-header">

                            <div className="response-avatar">
                                ✦
                            </div>

                            <div>

                                <strong>
                                    Nova
                                </strong>

                                <span>
                                    Just now
                                </span>

                            </div>

                        </div>


                        <p>
                            {reply}
                        </p>

                    </section>

                )}

            </main>


            <footer className="assistant-footer">

                <span>✦</span>

                Private & Personal

                <span>•</span>

                Nova AI

            </footer>

        </div>
    );
}


export default VoiceAssistant;