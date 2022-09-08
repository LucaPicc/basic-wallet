import { useCookies } from "react-cookie"

export const useAuth = () => {
    const [ cookie, setCookie ] = useCookies();

    const setAuth = (token, userid) => {
        setCookie('token', token, { path: '/' });
        setCookie('userid', userid, { path: '/' });
    }

    return {
        userid: cookie.userid,
        token: cookie.token,
        setAuth: setAuth,
        isAuth: cookie.userid && cookie.token
    }
}