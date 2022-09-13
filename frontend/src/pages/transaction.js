import { DEPOSIT, SEND, VALID_TRANSACTIONS, WITHDRAWAL } from "components/constants";

import DepositForm from "components/forms/deposit-form";
import SendForm from "components/forms/send-form";
import WithdrawalForm from "components/forms/withdrawal-form";
import { useParams } from "react-router-dom";

const getForm = (transaction) => {
    if (transaction === DEPOSIT) {
        return <DepositForm/>
    }

    if (transaction === SEND) {
        return <SendForm/>
    }

    if (transaction === WITHDRAWAL) {
        return <WithdrawalForm/>
    }
}

const Transaction = () => {
    const param = useParams();

    return (
        VALID_TRANSACTIONS.includes(param.transaction) ? (
            getForm(param.transaction)
        ) : <div>transaction not aviable</div>
    );
}

export default Transaction;
