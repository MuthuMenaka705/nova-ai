import { useState } from "react";

import Login from "./pages/Login";
import VoiceAssistant from "./pages/VoiceAssistant";
import Profile from "./pages/Profile";
import Reminders from "./pages/Reminders";


function App() {

    const [page, setPage] =
        useState("assistant");

    const [loggedIn, setLoggedIn] =
        useState(
            !!localStorage.getItem(
                "access_token"
            )
        );


    const handleLogin = () => {

        setLoggedIn(true);

        setPage("assistant");
    };


    const logout = () => {

        localStorage.removeItem(
            "access_token"
        );

        localStorage.removeItem(
            "refresh_token"
        );

        setLoggedIn(false);

        setPage("assistant");
    };


    /*
     * User is not logged in
     */
    if (!loggedIn) {

        return (
            <Login
                onLogin={handleLogin}
            />
        );
    }


    /*
     * Reminders page
     */
    if (page === "reminders") {

        return (
            <Reminders
                onBack={() =>
                    setPage("assistant")
                }
            />
        );
    }


    /*
     * Profile page
     */
    if (page === "profile") {

        return (
            <div className="app-shell">

                <Profile
                    onBack={() =>
                        setPage("assistant")
                    }
                />

            </div>
        );
    }


    /*
     * Main Nova assistant
     */
    return (
        <VoiceAssistant
            onLogout={logout}

            onOpenProfile={() =>
                setPage("profile")
            }

            onOpenReminders={() =>
                setPage("reminders")
            }
        />
    );
}


export default App;