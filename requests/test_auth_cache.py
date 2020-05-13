
from requests.auth_cache import MyLoginSession

if __name__ == "__main__":
    # proxies = {'https' : 'https://user:pass@server:port',
    #           'http' : 'http://user:pass@server:port'}

    loginData = {'user' : 'usr', 'password' :  'pwd'}

    loginUrl = 'https://...'
    loginTestUrl = 'https://...'
    successStr = 'Success'
    s = MyLoginSession(loginUrl, loginData, loginTestUrl, successStr, 
                       #proxies = proxies
                       )

    res = s.retrieveContent('https://....')
    print(res.text)

    # if, for instance, login via JSON values required try this:
    s = MyLoginSession(loginUrl, None, loginTestUrl, successStr, 
                       #proxies = proxies,
                       json = loginData)
