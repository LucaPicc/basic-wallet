import 'styles/login.css'

import LoginForm from 'components/forms/login-form';
import UserIcon from 'components/icons/user-icon';
import { useAuth } from 'hooks/useAuth';
import { useEffect } from 'react';

const LoginPage = () => {
    const { isAuth } = useAuth();

    useEffect(() => {
        if (isAuth) {
            return window.location = 'home'
        }
    }, [isAuth])

    return (
        <div className='container'>
            <div className='form_container'>
                <UserIcon width="40px" heigth="40px" />
                <h3 className='form_title'>LOGIN</h3>
                <h4 className='form_subtitle'>use your account information to login</h4>
                <LoginForm/>
            </div>
        </div>
    )
}

export default LoginPage;
