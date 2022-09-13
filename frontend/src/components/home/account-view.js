import 'styles/account.css';

import { Link } from 'react-router-dom';
import OperationsIcon from './transaction-card/operation-icon';
import { VALID_TRANSACTIONS } from 'components/constants';
import { getStyle } from './transaction-card/utils';
import { useAccount } from 'context/account-context';

const AccountView = () => {
    const { account } = useAccount();

    if (!account) return null

    return (
        <div className='account_container'>
            <div className='account_amount'>
                <div className='amount_title'>AMOUNT</div>
                <h2 className='amount_value'>{`${account.coin} ${account.balance}`}</h2>
            </div>
            <p className='amount_blocked'>{`USD ${account.funds_blocked} funds blocked`}</p>
            <p className='funds_to_be_settled'>{`USD ${account.funds_to_be_settled} funds to be settled`}</p>
            <div className='actions'>
                {
                    VALID_TRANSACTIONS.map((operation, index) =>(
                        <Link 
                            to={`/transaction/${operation}`} 
                            key={operation}
                            style={{...getStyle(operation), textDecoration: 'none', border:'none'}}
                        >
                            <OperationsIcon operation={operation}/>
                        </Link>
                    ))
                }
            </div>
        </div>
    )
}

export default AccountView;
