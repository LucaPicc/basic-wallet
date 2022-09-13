import 'styles/text-input.css'

import { useEffect, useState } from 'react'

import { getUsers } from 'api/api';
import { useAuth } from 'hooks/useAuth'

const UserSelector = ({label, type, props}) => {
    const { token, userid } = useAuth();
    const [ users, setUsers ] = useState([]);

    useEffect(() => {
        const fetchUsers = async () => {
            await getUsers(token, userid)
                .then((data) => {
                    setUsers(data)
                })
                .catch((error) => console.log(error))
        }
        fetchUsers();
    }, [token, userid])

    return (
        <div className='input_container'>
            <label className='input_label'>{label}</label>
            <select {...props} className='input_elem' type={type}>
                {
                    users.map((user, index) => (
                        <option value={user.id} key={index}>{user.username}</option>
                    ))
                }
            </select>
        </div>
    )
}

export default UserSelector