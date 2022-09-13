import 'styles/transactions-list.css'

import { useEffect, useState } from 'react';

import BasicCard from "components/basic-card";
import TransactionCard from './transaction-card/transaction-card';
import { getBlocked } from 'api/api';
import { useAuth } from 'hooks/useAuth';

const FundsSettledList = () => {
    const { token, userid } = useAuth();
    const [ blocked, setBlocked ] = useState([]);

    useEffect(() => {
        const fetchTransactions = async () => {
            await getBlocked(token, userid)
                .then((data) => setBlocked(data))
                .catch((error) => console.error(error))
        };

        fetchTransactions();
    },[token, userid])

    return (
        <BasicCard>
            <div className="list_head">FUNDS TO BE STTTED</div>
            <div className='list_body'>{
                blocked.map((block, index) => (
                    <TransactionCard
                        key={index}
                        amount={block.amount}
                        coin={block.coin}
                        created={block.created}
                        operation="block"
                        transmitter={block.transmitter}
                        code={block.code}
                    />
                ))
            }</div>
        </BasicCard>
    )
}

export default FundsSettledList;
