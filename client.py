import json
import requests
import requests_jwt

try:
    from config import credentials, urls
except ImportError:
    print('Config.py not found. Copy config.in to config.py and edit to suit.')
    exit()


def login(email, password):
    r = requests.post(urls.login,
                      json={"email": email,
                            "pass": password})
    r.raise_for_status()
    return r


def construct_jwt_auth(response):
    token = json.loads(response.text)['token']
    auth = requests_jwt.JWTAuth(token)
    return auth


def get_result_size(auth):
    headers = {"Range": "0-0"}
    r = requests.get(urls.data, auth=auth)
    size = int(r.headers['Content-Range'].split('/')[1])
    return size


def get_range(beg, end, page_size, auth):
    end = beg + page_size if beg + page_size < end else end
    this_range = '{0}-{1}'.format(beg, end)
    headers = {"Range": "{}".format(this_range)}
    r = requests.get(urls.data, auth=auth,
                     headers=headers)
    r.raise_for_status()
    return r.json()

if __name__ == '__main__':
    auth = construct_jwt_auth(login(credentials.email, credentials.password))
    size = get_result_size(auth)
    page_size = 20
    for i in range(0, size, page_size):
        this_range = get_range(i, i+page_size-1, page_size, auth)
        print(str(this_range) + '\n')
