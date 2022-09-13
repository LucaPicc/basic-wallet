import { createTransaction, getTransactions } from "api/api";
import { useEffect, useState } from "react";

import BasicCard from "components/basic-card";
import Button from "components/buttons/button";
import { useAuth } from "hooks/useAuth";
import { useParams } from "react-router-dom";

const ValidatePage = () => {
    const param = useParams();
    const { token, userid } = useAuth();
    const [ transaction, setTransaction ] = useState();

    const validateOperation = async () => {
        await createTransaction({
            operation: 'reception',
            transaction: transaction.id,
            userid: userid
        }, token)
            .then(() => (window.location = '/home/'))
    }

    useEffect(() => {
        const fetchTransaction = async () => {
            await getTransactions(token, userid, param.code)
                .then((data) => setTransaction(data))
                .catch((error) => console.error(error))
        }

        fetchTransaction();
    }, [token, userid, param])

    if (!transaction) return null

    console.log(transaction)

    return (
        <BasicCard>
            {transaction.code}
    const
            <Button onClick={validateOperation} label="ACCEPT"/>
        </BasicCard>
    )
}

export default ValidatePage;
