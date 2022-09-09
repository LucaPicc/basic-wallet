import 'styles/transactions-list.css'

import SendIcon from "components/icons/send-icon";

const TransactionCard = ({ amount, coin, code }) => {
    return (
        <div className="card">
            <div className="card_header">{code}</div>
            <div className="card_body">
                <div className="card_body__icon"><SendIcon width="30px" height="30px"/></div>
                <div className="info">{`${coin} ${amount}`}</div>
            </div>
        </div>
    );
}

export default TransactionCard;
