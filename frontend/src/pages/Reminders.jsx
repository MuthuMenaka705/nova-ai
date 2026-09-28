import {
    useEffect,
    useState,
} from "react";

import api from "../services/api";


function Reminders({
    onBack,
}) {

    const [reminders, setReminders] =
        useState([]);

    const [title, setTitle] =
        useState("");

    const [description, setDescription] =
        useState("");

    const [remindAt, setRemindAt] =
        useState("");

    const [loading, setLoading] =
        useState(false);


    const loadReminders = async () => {

        try {

            const response =
                await api.get(
                    "/reminders/"
                );

            setReminders(
                response.data
            );

        } catch (error) {

            console.error(error);
        }
    };


    useEffect(() => {

        loadReminders();

    }, []);


    const createReminder =
        async (event) => {

            event.preventDefault();

            if (!title || !remindAt) {
                return;
            }

            try {

                setLoading(true);

                await api.post(
                    "/reminders/",
                    {
                        title,
                        description,
                        remind_at: remindAt,
                    }
                );

                setTitle("");

                setDescription("");

                setRemindAt("");

                await loadReminders();

            } catch (error) {

                console.error(error);

            } finally {

                setLoading(false);
            }
        };


    const completeReminder =
        async (id) => {

            try {

                await api.patch(
                    `/reminders/${id}/`,
                    {
                        completed: true,
                    }
                );

                await loadReminders();

            } catch (error) {

                console.error(error);
            }
        };


    const deleteReminder =
        async (id) => {

            try {

                await api.delete(
                    `/reminders/${id}/`
                );

                await loadReminders();

            } catch (error) {

                console.error(error);
            }
        };


    return (
        <div className="profile-page">

            <div className="profile-card">

                <button
                    className="back-button"
                    onClick={onBack}
                >
                    ← Back to Nova
                </button>

                <h1>
                    Reminders
                </h1>

                <p className="profile-description">
                    Tell Nova what you need to
                    remember.
                </p>


                <form
                    onSubmit={
                        createReminder
                    }
                >

                    <div className="profile-field">

                        <label>
                            Reminder
                        </label>

                        <input
                            type="text"
                            value={title}
                            placeholder="Example: Drink water"
                            onChange={(event) =>
                                setTitle(
                                    event.target.value
                                )
                            }
                        />

                    </div>


                    <div className="profile-field">

                        <label>
                            Description
                        </label>

                        <input
                            type="text"
                            value={description}
                            placeholder="Optional"
                            onChange={(event) =>
                                setDescription(
                                    event.target.value
                                )
                            }
                        />

                    </div>


                    <div className="profile-field">

                        <label>
                            Reminder time
                        </label>

                        <input
                            type="datetime-local"
                            value={remindAt}
                            onChange={(event) =>
                                setRemindAt(
                                    event.target.value
                                )
                            }
                        />

                    </div>


                    <button
                        className="save-profile-button"
                        disabled={loading}
                    >
                        {loading
                            ? "Adding..."
                            : "Add Reminder"
                        }
                    </button>

                </form>


                <div className="reminder-list">

                    {reminders.map(
                        (reminder) => (

                            <div
                                className="reminder-item"
                                key={reminder.id}
                            >

                                <div>

                                    <strong>
                                        {reminder.title}
                                    </strong>

                                    <small>
                                        {reminder.remind_at}
                                    </small>

                                    {reminder.description && (
                                        <p>
                                            {
                                                reminder.description
                                            }
                                        </p>
                                    )}

                                </div>


                                {!reminder.completed && (

                                    <button
                                        onClick={() =>
                                            completeReminder(
                                                reminder.id
                                            )
                                        }
                                    >
                                        Done
                                    </button>

                                )}


                                <button
                                    onClick={() =>
                                        deleteReminder(
                                            reminder.id
                                        )
                                    }
                                >
                                    Delete
                                </button>

                            </div>

                        )
                    )}

                </div>

            </div>

        </div>
    );
}


export default Reminders;