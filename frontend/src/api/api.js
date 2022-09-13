export const getCoins = async (token) => {
    return fetch('http://localhost:8000/api/coin-list/', {
        method: 'GET',
        headers: new Headers({
            Authorization: `Token ${token}`,
            'Content-Type': 'application/json',
            Accept: 'application/json'
        })
    })
        .then((response) => (response.json()))
        .catch((error) => console.log(error))
}

export const login = async (data) => {
    return fetch('http://localhost:8000/auth/', {
        method: 'POST',
        mode: 'cors',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': '*/*'
        }),
        body: JSON.stringify({
            username: data.username,
            password: data.password
        })
    })
        .then((response) => response.json())
        .catch((error) => console.error(error))
}

export const createAccount = async (data) => {
    return fetch('http://localhost:8000/create_account/', {
        method: 'POST',
        mode: 'cors',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': '*/*'
        }),
        body: JSON.stringify(data)
    })
        .then((response) => response.json())
        .catch((error) => console.error(error))
}

export const getAccount = async (token, user_id) => {
    const url = `http://172.28.0.1:8000/api/account/?userid=${user_id}`
    return fetch(url, {
        method: 'GET',
        headers: new Headers({
            Authorization: `Token ${token}`,
            'Content-Type': 'application/json',
            Accept: 'application/json'
        })
    })
        .then((response) => (response.json()))
        .catch((error) => console.log(error))
}

export const createTransaction = async (data, token) => {
    return fetch('http://localhost:8000/api/transactions/', {
        method: 'POST',
        mode: 'cors',
        headers: new Headers({
            Authorization: `Token ${token}`,
            'Content-Type': 'application/json',
            'Accept': '*/*'
        }),
        body: JSON.stringify(data)
    })
        .then((response) => (response.json()))
        .catch((error) => console.error(error))
}

export const getUsers = (token, userid) => {
    return fetch(`http://localhost:8000/api/users/?userid=${userid}`, {
        method: 'GET',
        mode: 'cors',
        headers: new Headers({
            Authorization: `Token ${token}`,
            'Content-Type': 'application/json',
            'Accept': '*/*'
        }),
    })
        .then((response) => (response.json()))
        .catch((error) => console.error(error))
}

export const getTransactions = (token, userid, code) => {

    const url = code ? 
        `http://localhost:8000/api/transactions/?userid=${userid}&code=${code}` :
        `http://localhost:8000/api/transactions/?userid=${userid}`

    return fetch(url, {
        method: 'GET',
        mode: 'cors',
        headers: new Headers({
            Authorization: `Token ${token}`,
            'Content-Type': 'application/json',
            'Accept': '*/*'
        }),
    })
        .then((response) => (response.json()))
        .catch((error) => console.error(error))
}

export const getBlocked = (token, userid) => {
    
    return fetch(`http://localhost:8000/api/blocked/?userid=${userid}`, {
        method: 'GET',
        mode: 'cors',
        headers: new Headers({
            Authorization: `Token ${token}`,
            'Content-Type': 'application/json',
            'Accept': '*/*'
        }),
    })
        .then((response) => (response.json()))
        .catch((error) => console.error(error))
}
