import { createContext, useContext, useState } from "react";

const AccountContext = createContext({});

export const AccountContextProvider = ({children}) => {
    const [account, setAccount] = useState({});

    return (
        <AccountContext.Provider value={{ account: account, setAccount: setAccount }}>
            {children}
        </AccountContext.Provider>
    );
}

export const useAccount = () => useContext(AccountContext);