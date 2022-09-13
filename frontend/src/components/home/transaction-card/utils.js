import { BLOCK, DEPOSIT, RECEPTION, SEND, WITHDRAWAL } from "components/constants"

import BlockedIcon from "components/icons/blocked-icon"
import DepositIcon from "components/icons/deposit-icon"
import ReceptionIcon from "components/icons/reception-icon"
import SendIcon from "components/icons/send-icon"
import WithdrawalIcon from "components/icons/withdrawal-icon"

export const getIcon = (transaction) => {
    if (transaction === SEND) {
        return <SendIcon width="30px" height="30px"/>
    }

    if (transaction === DEPOSIT) {
        return <DepositIcon width="30px" height="30px" fill={getStyle(transaction).fill}/>
    }

    if (transaction === WITHDRAWAL) {
        return <WithdrawalIcon width="30px" height="30px" fill={getStyle(transaction).fill}/>
    }

    if (transaction === BLOCK) {
        return <BlockedIcon width="30px" height="30px" fill={getStyle(transaction).fill}/>
    }

    if (transaction === RECEPTION) {
        return <ReceptionIcon width="30px" height="30px" fill={getStyle(transaction).fill}/>
    }
}

export const getStyle = (transaction) => {
    if (transaction === SEND) {
        return {
            color: '#08b1db81'
        }
    }

    if (transaction === DEPOSIT) {
        return {
            border: 'solid 1px green',
            fill: 'green',
            color: 'green'
        }
    }

    if (transaction === WITHDRAWAL) {
        return {
            border: 'solid 1px red',
            fill: 'red',
            color: 'red'
        }
    }

    if (transaction === BLOCK) {
        return {
            border: 'solid 1px grey',
            fill: 'grey',
            color: 'grey'
        }
    }

    if (transaction === RECEPTION) {
        return {
            color: 'black'
        }
    }
} 