import 'styles/text-input.css'

import { useEffect, useState } from 'react';

import { getCoins } from 'api/api';
import { useAuth } from 'hooks/useAuth';

const CoinSelector = ({label, type, props}) => {
    const { token } = useAuth();
    const [ coins, setCoins ] = useState([]);
    
    useEffect(() => {
        const fetchCoins = async () => {
            await getCoins(token)
                .then((data) => setCoins(data))
                .catch((error) => console.error(error))
        }

        fetchCoins();
    }, [token])

    return (
        <div className='input_container'>
            <label className='input_label'>{label}</label>
            <select {...props} className='input_elem' type={type}>
                {
                    coins.map((coin) => (
                        <option key={coin.id} value={coin.id}>{coin.short_name}</option>
                    ))
                }
            </select>
        </div>
    )
}

export default CoinSelector;
