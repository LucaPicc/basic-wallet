import 'styles/account.css'

import LogoutIcon from 'components/icons/logout-icon';
import UserIcon from "components/icons/user-icon";
import { useAccount } from 'context/account-context';
import { useAuth } from 'hooks/useAuth';

const Head = () => {
    const { account } = useAccount();
    const { logout } = useAuth();


    if (!account) return null

    return (
        <div className='home_head'>
            <div className='home_head__start'>
            <div>hi {account.owner}!👋</div>
            </div>
            <div className='home_head__end'>
                <div style={{cursor: 'pointer'}} onClick={() => logout()}>
                    <LogoutIcon width="20px"/>
                </div>
            </div>
        </div>
    );
}

export default Head;
