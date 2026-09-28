import {
    useEffect,
    useState,
} from "react";

import api from "../services/api";


function Profile({
    onBack,
}) {

    const [profile, setProfile] =
        useState(null);

    const [saving, setSaving] =
        useState(false);

    const [message, setMessage] =
        useState("");


    useEffect(() => {

        loadProfile();

    }, []);


    const loadProfile = async () => {

        try {

            const response =
                await api.get(
                    "/profile/"
                );

            setProfile(
                response.data
            );

        } catch (error) {

            console.error(error);

            setMessage(
                "Could not load settings."
            );
        }
    };


    const saveProfile = async () => {

        if (!profile) {
            return;
        }


        try {

            setSaving(true);

            setMessage("");


            const response =
                await api.patch(
                    "/profile/",
                    {
                        display_name:
                            profile.display_name,

                        timezone:
                            profile.timezone,

                        proactive_enabled:
                            profile.proactive_enabled,

                        quiet_hours_start:
                            profile.quiet_hours_start,

                        quiet_hours_end:
                            profile.quiet_hours_end,
                    }
                );


            setProfile(
                response.data
            );


            setMessage(
                "Settings saved."
            );


        } catch (error) {

            console.error(error);

            setMessage(
                "Could not save settings."
            );

        } finally {

            setSaving(false);
        }
    };


    if (!profile) {

        return (
            <div className="profile-page">

                <div className="profile-card">

                    <p>
                        Loading Nova settings...
                    </p>

                </div>

            </div>
        );
    }


    return (
        <div className="profile-page">

            <div className="profile-card">

                <button
                    className="back-button"
                    onClick={onBack}
                >
                    ← Back to Nova
                </button>


                <div className="profile-icon">
                    ✦
                </div>


                <h1>
                    Nova Settings
                </h1>


                <p className="profile-description">
                    Control how Nova interacts
                    with you.
                </p>


                <div className="profile-field">

                    <label>
                        Display name
                    </label>

                    <input
                        type="text"
                        value={
                            profile.display_name ||
                            ""
                        }
                        onChange={(event) =>
                            setProfile({
                                ...profile,
                                display_name:
                                    event.target.value,
                            })
                        }
                    />

                </div>


                <div className="profile-field">

                    <label>
                        Timezone
                    </label>

                    <input
                        type="text"
                        value={
                            profile.timezone ||
                            ""
                        }
                        onChange={(event) =>
                            setProfile({
                                ...profile,
                                timezone:
                                    event.target.value,
                            })
                        }
                    />

                </div>


                <label className="profile-toggle">

                    <input
                        type="checkbox"
                        checked={
                            profile.proactive_enabled
                        }
                        onChange={(event) =>
                            setProfile({
                                ...profile,
                                proactive_enabled:
                                    event.target.checked,
                            })
                        }
                    />

                    <span>
                        Allow Nova to proactively
                        speak
                    </span>

                </label>


                <div className="profile-field">

                    <label>
                        Quiet hours start
                    </label>

                    <input
                        type="time"
                        value={
                            profile.quiet_hours_start ||
                            ""
                        }
                        onChange={(event) =>
                            setProfile({
                                ...profile,
                                quiet_hours_start:
                                    event.target.value,
                            })
                        }
                    />

                </div>


                <div className="profile-field">

                    <label>
                        Quiet hours end
                    </label>

                    <input
                        type="time"
                        value={
                            profile.quiet_hours_end ||
                            ""
                        }
                        onChange={(event) =>
                            setProfile({
                                ...profile,
                                quiet_hours_end:
                                    event.target.value,
                            })
                        }
                    />

                </div>


                <button
                    className="save-profile-button"
                    onClick={saveProfile}
                    disabled={saving}
                >

                    {saving
                        ? "Saving..."
                        : "Save Settings"
                    }

                </button>


                {message && (

                    <div className="profile-message">
                        {message}
                    </div>

                )}

            </div>

        </div>
    );
}


export default Profile;