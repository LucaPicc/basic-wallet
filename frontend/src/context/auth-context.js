import { createContext, useContext, useState } from "react";

const AuthContext = createContext({});

export const AuthContextProvider = ({children}) => {
    const [auth, setAuth] = useState({});

    return (
        <AuthContext.Provider value={{ auth:auth, setAuth: setAuth }}>
            {children}
        </AuthContext.Provider>
    );
}

export const useAuth = () => useContext(AuthContext);
