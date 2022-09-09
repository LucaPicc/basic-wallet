import 'styles/home.css'

import AccountView from 'components/home/account-view';
import Head from 'components/home/head';
import TransactionsList from 'components/home/transactions-list';
import { useAccount } from 'hooks/useAccount';
import { useEffect } from 'react';

const HomePage = () => {
    const { fetchAccount } = useAccount();

    useEffect(() => {
        fetchAccount();
    }, [fetchAccount])
    
    return (
        <div>
            <Head/>
            <AccountView/>
            <TransactionsList/>
        </div>
    );
}

export default HomePage;
