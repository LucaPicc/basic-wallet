import 'styles/transactions-list.css'

import { BLOCK, SEND } from 'components/constants';

import BasicCard from 'components/basic-card';
import { Link } from 'react-router-dom';
import OperationsIcon from './operation-icon';
import { getStyle } from './utils';

const TransactionCard = ({ amount, coin, code, operation, created, receiver, transmitter }) => {
    return (
        <BasicCard style={getStyle(operation)}>
            <div className="card_header">
                <div>
                    {code}
                </div>
                <div>{created}</div>
                {
                    operation === SEND && (
                        <div>{`receiver: ${receiver}`}</div>
                    )
                }
                {
                    operation === BLOCK && (
                        <div>{`transmitter: ${transmitter}`}</div>
                    )
                }
            </div>
            <div className="card_body">
                <OperationsIcon operation={operation}/>
                <div className="info">{`${coin} ${amount}`}</div>
            </div>
            {
                operation === BLOCK && (
                    <Link to={`/validate/${code}`} key={code}>VALIDATE</Link>
                )
            }
        </BasicCard>
    );
}

export default TransactionCard;
