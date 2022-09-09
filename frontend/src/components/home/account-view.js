import 'styles/account.css';

import DepositIcon from 'components/icons/deposit-icon';
import { Link } from 'react-router-dom';
import { useAccount } from 'hooks/useAccount';

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
            <Link to="/transaction/deposit" key="deposit" className="deposit-action">
                <DepositIcon width="12px"/>DEPOSIT
            </Link>

        </div>
    )
}

export default AccountView;
