import "styles/deposit_form.css"

import BasicCard from "components/basic-card";
import Button from "components/buttons/button";
import CoinSelector from "./input/coin-selector";
import TextInput from "./input/text-input";
import UserSelector from "./input/user-selector";
import { createTransaction } from "api/api";
import { useAuth } from "hooks/useAuth";
import { useForm } from "react-hook-form";

const SendForm = () => {
    const { token, userid } = useAuth();
    const { register, handleSubmit, watch, formState: { errors } } = useForm();

    const onSubmit = async (data) => {
        await createTransaction(
            {
                operation: 'send',
                transmitter: userid,
                ...data 
            },
            token
        )
            .then((data) => {
                return window.location = '/home/'
            })
            .catch((error) => console.error(error))
    }

    const onCancel = () => (window.location = '/home/')

    return (
        <BasicCard>
            <form onSubmit={handleSubmit(onSubmit)} className="deposit_form">
                <UserSelector label="receiver" props={register('receiver', { required: true })}/>
                <CoinSelector label="coin" props={register('coin', { required: true })}/>
                <TextInput label="amount" type="number" props={register('amount', { required: true })}/>
                <div className="deposit_form__action">
                    <Button label="SEND" type='submit'/>
                    <Button label="CANCEL" onClick={onCancel}/>
                </div>
            </form>
        </BasicCard>
    )
}

export default SendForm;
