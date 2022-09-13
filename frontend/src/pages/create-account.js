import 'styles/login.css'

import CreateAccountForm from 'components/forms/create-account-form';
import UserIcon from 'components/icons/user-icon';
import { useAuth } from 'hooks/useAuth';
import { useEffect } from 'react';

const CreateAccountPage = () => {
    const { isAuth } = useAuth();

    useEffect(() => {
        if (isAuth) {
            return window.location = '/home/'
        }
    }, [isAuth])

    return (
        <div className='container'>
            <div className='form_container'>
                <UserIcon width="40px" heigth="40px" />
                <h3 className='form_title'>CREATE ACCOUNT</h3>
                <CreateAccountForm/>
            </div>
        </div>
    )
}

export default CreateAccountPage;
