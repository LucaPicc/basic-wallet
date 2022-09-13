import { getIcon, getStyle } from "./utils";

const OperationsIcon = ({operation}) => {
    
    return (
        <div className='card_body__operation'>
            <div className="card_body__icon" style={getStyle(operation)}>
                {getIcon(operation)}
            </div>
            <div className='operation_info'>{operation}</div>
        </div>
    )
}

export default OperationsIcon