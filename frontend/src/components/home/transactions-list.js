import 'styles/transactions-list.css';

import { useEffect, useState } from 'react';

import BasicCard from 'components/basic-card';
import TransactionCard from './transaction-card/transaction-card';
import { getTransactions } from 'api/api';
import { useAuth } from 'hooks/useAuth';

const TransactionsList = () => {
    const { token, userid } = useAuth();
    const [ transactions, setTransactions ] = useState([])

    useEffect(() => {
        const fetchTransactions = async () => {
            await getTransactions(token, userid)
                .then((data) => setTransactions(data))
                .catch((error) => console.error(error))
        }

        fetchTransactions();
    }, [token, userid])

    return (
        <BasicCard>
            <div className='list_head'>TRANSACTIONS</div>
            <div className='list_body'>{
                transactions.map((trans, index) => (
                    <TransactionCard
                        key={index}
                        operation={trans.operation}
                        coin={trans.coin}
                        code={trans.code}
                        amount={trans.amount}
                        created={trans.created}
                        receiver={trans.receiver}
                    />
                ))
            }</div>
        </BasicCard>
    )
};

export default TransactionsList;
