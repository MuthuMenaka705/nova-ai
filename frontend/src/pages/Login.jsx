import { useState } from "react";

import api from "../services/api";


function Login({ onLogin }) {

    const [username, setUsername] =
        useState("");

    const [password, setPassword] =
        useState("");

    const [error, setError] =
        useState("");

    const [loading, setLoading] =
        useState(false);


    const login = async (event) => {

        event.preventDefault();

        setError("");

        setLoading(true);


        try {

            const response =
                await api.post(
                    "/auth/login/",
                    {
                        username,
                        password,
                    }
                );


            localStorage.setItem(
                "access_token",
                response.data.access
            );


            localStorage.setItem(
                "refresh_token",
                response.data.refresh
            );


            onLogin();

        } catch (error) {

            console.error(error);

            setError(
                "Username or password is incorrect."
            );

        } finally {

            setLoading(false);
        }
    };


    return (
        <div className="login-page">

            <div className="login-card">

                <div className="login-logo">
                    ✦
                </div>


                <h1>
                    Welcome to Nova
                </h1>


                <p className="login-subtitle">
                    Your personal AI assistant
                </p>


                <form
                    onSubmit={login}
                >

                    <div className="login-field">

                        <label>
                            Username
                        </label>

                        <input
                            type="text"
                            placeholder="Enter your username"
                            value={username}
                            onChange={(event) =>
                                setUsername(
                                    event.target.value
                                )
                            }
                            required
                        />

                    </div>


                    <div className="login-field">

                        <label>
                            Password
                        </label>

                        <input
                            type="password"
                            placeholder="Enter your password"
                            value={password}
                            onChange={(event) =>
                                setPassword(
                                    event.target.value
                                )
                            }
                            required
                        />

                    </div>


                    {error && (

                        <div className="login-error">
                            {error}
                        </div>

                    )}


                    <button
                        className="login-button"
                        type="submit"
                        disabled={loading}
                    >

                        {loading
                            ? "Signing in..."
                            : "Sign in to Nova"
                        }

                    </button>

                </form>


                <div className="login-footer">

                    <span>✦</span>

                    <span>
                        Private • Personal • Intelligent
                    </span>

                </div>

            </div>

        </div>
    );
}


export default Login;