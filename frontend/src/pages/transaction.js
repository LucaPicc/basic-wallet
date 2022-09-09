import DepositForm from "components/forms/deposit-form";
import { useParams } from "react-router-dom";

const Transaction = () => {
    const param = useParams();

    return (
        param.transaction === 'deposit' ? (
            <DepositForm/>
        ) : <div>transaction not aviable</div>
    );
}

export default Transaction;
