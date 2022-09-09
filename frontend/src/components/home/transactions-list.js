import 'styles/transactions-list.css'

import SendIcon from 'components/icons/send-icon';
import TransactionCard from './transaction-card';

const TransactionsList = () => {
    const transactions_list = [
        {
            operation: 'send',
            amount: 1000,
            coin: 'USD',
            code: 'askjdha7856as7fasfg78w'
        },
        {
            operation: 'send',
            amount: 1000,
            coin: 'USD',
            code: 'askjdha7856as7fasfg78w'
        },
        {
            operation: 'send',
            amount: 1000,
            coin: 'USD',
            code: 'askjdha7856as7fasfg78w'
        }
    ]

    return (
        <div className='list_container'>
            <div className='list_head'>TRANSACTIONS</div>
            <div className='list_body'>{
                transactions_list.map((trans, index) => (
                    <TransactionCard
                        key={index}
                        operation={trans.operation}
                        coin={trans.coin}
                        code={trans.code}
                        amount={trans.amount}
                    />
                ))
            }</div>
        </div>
    )
};

export default TransactionsList;
