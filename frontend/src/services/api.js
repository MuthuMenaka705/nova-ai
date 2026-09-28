import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api",
    headers: {
        "Content-Type": "application/json",
    },
});

api.interceptors.request.use(
    (config) => {
        const token =
            localStorage.getItem("access_token");

        if (token) {
            config.headers.Authorization =
                `Bearer ${token}`;
        }

        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

api.interceptors.response.use(
    (response) => response,

    async (error) => {
        if (
            error.response &&
            error.response.status === 401
        ) {
            const refreshToken =
                localStorage.getItem(
                    "refresh_token"
                );

            if (refreshToken) {
                try {
                    const response =
                        await axios.post(
                            "http://127.0.0.1:8000/api/auth/refresh/",
                            {
                                refresh:
                                    refreshToken,
                            }
                        );

                    const newAccessToken =
                        response.data.access;

                    localStorage.setItem(
                        "access_token",
                        newAccessToken
                    );

                    error.config.headers.Authorization =
                        `Bearer ${newAccessToken}`;

                    return api(error.config);

                } catch (refreshError) {
                    localStorage.removeItem(
                        "access_token"
                    );

                    localStorage.removeItem(
                        "refresh_token"
                    );

                    window.location.reload();
                }
            }
        }

        return Promise.reject(error);
    }
);

export default api;