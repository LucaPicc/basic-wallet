import { getAccount } from "api/api"
import { useAuth } from "./useAuth"

export const useAccount = () => {
    const { userid, token } = useAuth()

    const fetchAccount = async () => {
        await getAccount(token, userid)
            .then((data) => {
                sessionStorage.setItem('owner', data.owner);
                sessionStorage.setItem('balance', data.balance);
                sessionStorage.setItem('cvu', data.cvu);
                sessionStorage.setItem('coin', data.coin);
                sessionStorage.setItem('funds_blocked', data.funds_blocked)
                sessionStorage.setItem('funds_to_be_settled', data.funds_to_be_settled)
            })
            .catch((error) => console.error(error))
    }

    return {
        account: {
            owner: sessionStorage.getItem('owner'),
            balance: sessionStorage.getItem('balance'),
            cvu: sessionStorage.getItem('cvu'),
            coin: sessionStorage.getItem('coin'),
            funds_blocked: sessionStorage.getItem('funds_blocked'),
            funds_to_be_settled: sessionStorage.getItem('funds_to_be_settled')
        },
        fetchAccount: fetchAccount
    }
}
