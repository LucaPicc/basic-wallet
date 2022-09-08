import 'styles/login.css';

import Button from 'components/buttons/button';
import TextInput from './input/text-input';
import { login } from 'api/api';
import { useAuth } from 'hooks/useAuth';
import { useForm } from 'react-hook-form';

const LoginForm = () => {
    const { register, handleSubmit, watch, formState: { errors } } = useForm();
    const { setAuth } = useAuth();

    const onSubmit = async (data) => {
        await login(data)
            .then((auth) => {
                setAuth(auth.token, auth.userid);
            })
            .catch((_errors) => {
                errors.login = 'incorrect information'
            })
    }

    return (

        <form onSubmit={handleSubmit(onSubmit)} className='form_input_container'>
            <TextInput label='username' type={'text'} props={register('username', { required: true })} />
            <TextInput label='password' type={'password'} props={register('password', { required: true })} />
            <div className='form_keypad'>
                <Button label='LOGIN' type='submit' />
                <Button label='SIGIN' />
            </div>
            <div className='display_erros'>
                {
                    errors.username && (
                        <p>username is required</p>
                    )
                }
                {
                    errors.password && (
                        <p>password is required</p>
                    )
                }
                {
                    errors.login && (
                        <p>errors.login</p>
                    )
                }
            </div>
        </form>
    );
}

export default LoginForm