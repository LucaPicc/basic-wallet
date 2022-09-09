import { createContext, useContext, useState } from "react";

const AccountContext = createContext({});

export const AccountContextProvider = ({children}) => {
    const [auth, setAuth] = useState({});

    return (
        <AccountContext.Provider value={{ auth:auth, setAuth: setAuth }}>
            {children}
        </AccountContext.Provider>
    );
}

export const useAuth = () => useContext(AccountContext);