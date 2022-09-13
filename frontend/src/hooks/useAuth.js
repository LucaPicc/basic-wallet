import { useCookies } from "react-cookie"

export const useAuth = () => {
    const [ cookie, setCookie, removeCookie ] = useCookies();

    const setAuth = (token, userid) => {
        setCookie('token', token, { path: '/' });
        setCookie('userid', userid, { path: '/' });
    }

    const logout = () => {
        removeCookie('token', { path: '/' });
        removeCookie('userid', { path: '/' });
        return window.location = '/'
    }

    return {
        userid: cookie.userid,
        token: cookie.token,
        setAuth: setAuth,
        isAuth: cookie.userid && cookie.token,
        logout: logout
    }
}