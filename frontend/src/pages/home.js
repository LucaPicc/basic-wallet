import 'styles/home.css'

import AccountView from 'components/home/account-view';
import FundsSettledList from 'components/home/funds-settled-list';
import Head from 'components/home/head';
import TransactionsList from 'components/home/transactions-list';
import { getAccount } from 'api/api';
import { useAccount } from 'context/account-context';
import { useAuth } from 'hooks/useAuth';
import { useEffect } from 'react';

const HomePage = () => {    
    const { token, userid } = useAuth();
    const { setAccount } = useAccount();

    useEffect(() => {
        const fetchAccount = async () => {
            await getAccount(token, userid)
                .then((data) => {
                    setAccount({
                        owner: data.owner,
                        balance: data.balance,
                        cvu: data.cvu,
                        coin: data.coin,
                        funds_blocked: data.funds_blocked,
                        funds_to_be_settled: data.funds_to_be_settled
                    })
                })
                .catch((error) => console.error(error))
        }

        fetchAccount()
    }, [setAccount, token, userid])
    
    return (
        <div>
            <Head/>
            <div className='home_body'>
                <AccountView/>
                <FundsSettledList/>
                <TransactionsList/>

            </div>
        </div>
    );
}

export default HomePage;
