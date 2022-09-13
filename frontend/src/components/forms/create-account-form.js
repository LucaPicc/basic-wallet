import 'styles/login.css';

import Button from 'components/buttons/button';
import { Link } from 'react-router-dom';
import TextInput from './input/text-input';
import { createAccount } from 'api/api';
import { useAuth } from 'hooks/useAuth';
import { useForm } from 'react-hook-form';

const CreateAccountForm = () => {
    const { register, handleSubmit, watch, formState: { errors } } = useForm();
    const { setAuth } = useAuth();

    const onSubmit = async (data) => {
        await createAccount(data)
            .then((auth) => {
                setAuth(auth.token, auth.userid);
            })
            .catch((_errors) => {
                errors.login = 'incorrect information'
            })
    }

    return (
        <form onSubmit={handleSubmit(onSubmit)} className='form_input_container'>
            <TextInput label='first name' type={'text'} props={register('first-name', { required: true })} />
            <TextInput label='last name' type={'text'} props={register('last-name', { required: true })} />
            <TextInput label='email' type={'email'} props={register('email', { required: true })} />
            <TextInput label='password' type={'password'} props={register('password', { required: true })} />
            <div className='form_keypad'>
                <Button label='SIGIN' type='submit'/>
                <Link to={'/'}>CANCEL</Link>
            </div>
        </form>
    );
}

export default CreateAccountForm