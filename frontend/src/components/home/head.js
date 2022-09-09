import 'styles/account.css'

import UserIcon from "components/icons/user-icon";
import { useAccount } from "hooks/useAccount";

const Head = () => {
    const { account } = useAccount();

    if (!account) return null

    return (
        <div className='home_head'>
            <div className='home_head__start'>
            <div>hi {account.owner}!👋</div>
            </div>
            <div className='home_head__end'>
                <div><UserIcon width="20px"/></div>
            </div>
        </div>
    );
}

export default Head;
