import 'styles/account.css';

import { getAccount, getCoins } from 'api/api';
import { useEffect, useState } from 'react';

import { useAuth } from 'hooks/useAuth';

const AccountView = () => {
    const { userid, token, isAuth } = useAuth();
    const [ accountInfo, setAccountInfo ] = useState({});

    useEffect(() => {
        if (!isAuth) {
            return window.location='/'
        }

        const getInfo = async () => {
            await getAccount(token, userid)
                .then((info) => setAccountInfo(info))
                .catch((error) => console.error(error))
        }

        getInfo();

    }, [isAuth, token, userid])

    if (!accountInfo) return null

    return (
        <div className='account_container'>
            <h2 className='title'>Hi {accountInfo.owner}!👋</h2>
        </div>
    )
}

export default AccountView;
