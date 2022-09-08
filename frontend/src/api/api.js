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

export const getAccount = async (token, user_id) => {
    const url = `http://localhost:8000/api/account/?userid=${user_id}`
    return fetch(url , {
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